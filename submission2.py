import torch
from util.util import bench_acc,bench_speed

torch.backends.cudnn.benchmark = True
torch.backends.cudnn.deterministic = True
torch.cuda.cudnn_enabled = True

########################################################
#Define and initialize your model herer
########################################################

from torch2trt import torch2trt,TRTModule  

model = TRTModule()
model.load_state_dict(torch.load('./submission2/model_trt.pth'))

########################################################
#Run and evaluate
########################################################

mean_iu = bench_acc(model)
speed = bench_speed(model)


print('[With TensorRT] mIoU: {} ; Speed : {} ms/f'.format(mean_iu, speed))


