import torch
from util.util import bench_acc,bench_speed

torch.backends.cudnn.benchmark = True
torch.backends.cudnn.deterministic = True
torch.cuda.cudnn_enabled = True

########################################################
#Define and initialize your model herer
########################################################
from submission1.fanet import FANet

model = FANet()   
model.load_state_dict(torch.load('./submission1/model.pkl'))
model.eval()
model.cuda()

########################################################
#Run and evaluate
########################################################

mean_iu = bench_acc(model)
speed = bench_speed(model)
power = 0.0#bench_power(model)

print('mIoU: {:04f}; Speed : {:06f} s/f; Avg Power : {:06f} mJ/f'.format(mean_iu, speed, power))

