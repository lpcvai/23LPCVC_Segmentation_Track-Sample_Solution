### LPCVC2023 Sample Solution

## How to Run

The following sections cover how to setup the sample solution.

### Dependencies

The evaluation of these sample models is dependent upon
[`Python 3.6`](https://www.python.org/downloads/release/python-3109/)

The following `Python 3.6` dependencies will be installed on the nanos:

- `certifi==2021.5.30`
- `dataclasses==0.8`
- `imageio==2.15.0`
- `numpy==1.19.5`
- `opencv-python==4.7.0.72`
- `Pillow==8.4.0`
- `torch==1.10.1`
- `torchvision==0.11.2`
- `typing_extensions==4.1.1`

## Compressing to pyz
python3.6 -m zipapp  solution  -p='/usr/bin/env python3.6'

## Formatting

This is the directory tree from our sample solution and in correspondance with the path we used for our model.
```
lpcvc2023_sample_solution
├── __init__.py
├── __main__.py
├── main.py
├── model.pkl
├── README.md
└── utils
    ├── fanet.py
    ├── __init__.py
    ├── README.md
    └── resnet.py
```

## Evaluation
We will be evaluating your file in using the evaluation folder provided.

## Run Solution
The Solution should be able to be ran with the command: `python3.6 solution.pyz -i /path/to/image -o /path/to/output.png`