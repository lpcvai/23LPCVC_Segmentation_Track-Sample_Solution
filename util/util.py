# Adapted from score written by wkentaro
# https://github.com/wkentaro/pytorch-fcn/blob/master/torchfcn/utils.py

import numpy as np
import os
import torch
import tqdm,time
import imageio as imageio
import cv2
import torchvision.transforms as transforms
import torch.nn.functional as F
import subprocess
from threading import  Thread, Event
import jtop

MEAN = (0.485, 0.456, 0.406)
STD = (0.229, 0.224, 0.225)
SIZE = [512,512]
####################################################################

class runningScore(object):
    def __init__(self, n_classes):
        self.n_classes = n_classes
        self.confusion_matrix = np.zeros((n_classes, n_classes))

    
    def reset(self):
        self.confusion_matrix = np.zeros((self.n_classes, self.n_classes))

    def _fast_hist(self, label_true, label_pred, n_class):
        mask = (label_true >= 0) & (label_true < n_class)
        hist = np.bincount(
            n_class * label_true[mask].astype(int) + label_pred[mask], minlength=n_class ** 2
        ).reshape(n_class, n_class)
        return hist

    def update(self, label_trues, label_preds):
        for lt, lp in zip(label_trues, label_preds):
            self.confusion_matrix += self._fast_hist(lt.flatten(), lp.flatten(), self.n_classes)

    def get_scores(self):
        """Returns accuracy score evaluation result.
            - overall accuracy
            - mean accuracy
            - mean IU
            - fwavacc
        """
        hist = self.confusion_matrix
        self.acc = np.diag(hist).sum() / hist.sum()
        acc_cls = np.diag(hist) / (hist.sum(axis=1)+0.000000001)
        self.acc_cls = np.nanmean(acc_cls)
        iu = np.diag(hist) / (hist.sum(axis=1) + hist.sum(axis=0) - np.diag(hist))
        self.mean_iu = np.nanmean(iu)
        freq = hist.sum(axis=1) / hist.sum()
        self.fwavacc = (freq[freq > 0] * iu[freq > 0]).sum()
        self.cls_iu = dict(zip(range(self.n_classes), iu))

        return (
            {
                "Overall Acc: \t": self.acc,
                "Mean Acc : \t": self.acc_cls,
                "FreqW Acc : \t": self.fwavacc,
                "Mean IoU : \t": self.mean_iu,
            }
        )

class averageMeter(object):
    """Computes and stores the average and current value"""

    def __init__(self, sstep=0):
        self.reset()
        self.sstep = sstep

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):

        self.count += n
        if self.count>= self.sstep: 
            self.val = val
            self.sum += val * n
            self.avg = self.sum / (self.count-self.sstep+1)

def bench_acc(model, dataPath='./data/'):
    #[input] model: segmenation model
    #[input] dataPath: path to a folder containing 'gt' and 'img'
    #[input] accMeter: measure mIoU

    accMeter = runningScore(n_classes=14)

    files = os.listdir(dataPath+'IMG/')

    imgList = []
    gtList = []

    for i, imgName in enumerate(files):
        imgPath = dataPath+'IMG/'+ imgName
        gtPath = dataPath+'GT/'+ imgName

        npyImg = imageio.imread(imgPath)
        npyGT =  imageio.imread(gtPath).astype(np.uint8)

        npyImg = cv2.resize(npyImg, tuple(SIZE), interpolation = cv2.INTER_AREA)
        npyGT = cv2.resize(npyGT, tuple(SIZE), interpolation = cv2.INTER_NEAREST)
        npyGT = npyGT[np.newaxis,:,:]

        tenImg = transforms.ToTensor()(npyImg)  # convert to tensor (values between 0 and 1)
        tenImg = transforms.Normalize(MEAN, STD)(tenImg)  # normalize the tensor
        tenImg = tenImg.unsqueeze(0)  # add a batch dimension

        tenOut = model(tenImg.cuda())  #testing
        tenOut = F.interpolate(tenOut, (SIZE[1],SIZE[0]), mode='bilinear', align_corners=True)
        npyOut = tenOut.cpu().data.max(1)[1].numpy()


        accMeter.update(npyGT, npyOut)

    accMeter.get_scores()

    return accMeter.mean_iu

def bench_speed(model, iter=30):
    #[input] model: segmenation model
    #[input] iter: number of iteration for benchmarking

    runtimeMeter = averageMeter(10)

    input = torch.rand((1,3,SIZE[1],SIZE[0])).cuda()

    for idx in range(iter):

        torch.cuda.synchronize()
        t_0 = time.time()

        tenOut = model(input)  #testing

        torch.cuda.synchronize()
        t_1 = time.time()
        
        runtimeMeter.update(t_1-t_0)

    return runtimeMeter.avg

def bench_power(model, iter=200):

    powerMeter = averageMeter(20)

    end_event = Event()
    cnt_event = Event()

    def powermeter(powerMeter): 

        with jtop.jtop() as jtsn:
            while True:
                if end_event.is_set():
                    break
    
                if cnt_event.is_set():
                    time.sleep(0.01)
                    out = float(jtsn.power[1]['5V GPU']['cur'])
                    powerMeter.update(out)

    thread = Thread(target=powermeter, args=(powerMeter,))
    thread.start()

    input = torch.rand((1,3,SIZE[1],SIZE[0])).cuda()

    for idx in range(iter):

        tenOut = model(input)  #testing
        torch.cuda.synchronize()
        cnt_event.set()

    torch.cuda.synchronize()

    end_event.set()

    return powerMeter.avg
