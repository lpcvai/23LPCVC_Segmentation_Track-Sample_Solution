# Sample Solution for LPCVC2023

## Environment
- imageio==2.15.0
- jetson_stats==3.0.1
- numpy==1.19.2
- torch==1.4.0
- torchvision==0.2.2.post3
- tqdm==4.64.1

## Testing Data 
- Download [testing data](https://drive.google.com/file/d/1bBwwA_SQ4vT7p5dBuZwo3rMipI6fx7SC/view?usp=share_link) (Please keep this confidential and don't distribute)
- Organize testing directory as
```
├── util
|── README.md
|── submission1
|── submission1.py
|── submission2
|── submission2.py
└── data
    └── IMG
        ├── test_0000.png
        ├── test_0001.png
        ├── ...
        └── test_0499.png
    └── GT
        ├── test_0000.png
        ├── test_0001.png
        ├── ...
        └── test_0499.png
```  

## Evaluation
### Format
- Input/output resolution: 512*512
- Model Output: 14 \* 512 \* 512 for *Channel \* Height \* Width*. Each channel corresponds to the predicted probability for one category.
### Metrics
- Accuracy: mIoU over all th 14 categories. By calling function `bench_acc()`.
- Speed: average runtime for processing one frame (s/f). By calling function `bench_speed()`.
- Power: power consumption of GPU for processing one frame (s/f). By calling function `bench_power()`.

## Submission
For a submission *MODEL*, there are should be
- *MODEL.py*: a formated file for performing evaluation 
- *MODEL*: a folder containin related model files, weights, etc.

### Sample-1
- Run `python submission1.py` 
- `submission1` is plain pytorch model

### Sample-2 (We will provide this as the examplar solution)
- Run `python submission2.py` 
- `submission2` is tenorRT model converted from Sample-1.

