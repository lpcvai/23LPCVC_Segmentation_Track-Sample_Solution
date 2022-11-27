import torch
from util.util import bench_acc,bench_speed,bench_power

torch.backends.cudnn.benchmark = True
torch.backends.cudnn.deterministic = True
torch.cuda.cudnn_enabled = True

########################################################
#Define and initialize your model herer
########################################################

import torch2trt

model = torch2trt.TRTModule()
model.load_state_dict(torch.load('./submission2/model_trt.pkl')) #check  ../submission1/save_trt.py for generating model_trt.pkl

########################################################
#Run and evaluate
########################################################

mean_iu = 0#bench_acc(model)
speed = bench_speed(model)
power = bench_power(model)

print('mIoU: {:04f}; Speed : {:06f} s/f; Avg Power : {:06f} mJ/f'.format(mean_iu, speed, power))