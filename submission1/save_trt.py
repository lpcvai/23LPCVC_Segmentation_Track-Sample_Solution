import torch
from fanet import FANet
from torch2trt import torch2trt  

SIZE = [512,512]

model = FANet()   
model.load_state_dict(torch.load('./model.pkl'))
model.eval()
model.cuda()
model_trt = torch2trt(model, [torch.rand((1,3,SIZE[1],SIZE[0])).cuda()], fp16_mode=True)

torch.save(model_trt.state_dict(),'model_trt.pkl')