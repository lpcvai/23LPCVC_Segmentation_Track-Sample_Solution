### LPCVC2023 Sample Solution

## How to Run

The following sections cover how run the sample solution.

### Dependencies

The evaluation of these sample models is dependent upon
[`Python 3.10`](https://www.python.org/downloads/release/python-3109/)

The following `Python 3.6` dependencies will be installed on the evaluation nanos:

- `certifi==2021.5.30`
- `dataclasses==0.8`
- `imageio==2.15.0`
- `numpy==1.19.5`
- `opencv-python==4.7.0.72`
- `Pillow==8.4.0`
- `torch==1.10.1`
- `torchvision==0.11.2`
- `typing_extensions==4.1.1`

We provide a [`requirements.txt`](requirements.txt) file that can be used to
install the dependencies with the following commands:

1. `python3.10 -m pip install --upgrade pip`
1. `python3.10 -m pip install -r requirements.txt`

## Directory Structure

Here is the directory structure that will be used to evaluate solutions. The test directory will need images added.
```
evaluation
├── accuracy.py
├── evaluation.bash
├── main.py
├── output
├── README.md
├── sample_solution.pyz
└── test
    ├── GT
    │   ├── img_0000.png
    │   └── img_0001.png
    └── IMG
        ├── img_0000.png
        └── img_0001.png
```
## Metrics
- Accuracy will be measured using the Accuracy.py script. In this script we make a NclassxNclass Confusion matrix out of the inputted segmentation map and ground truth. This confusion matrix is used to calculate the dice coefficient using the formula:

- Speed will be measured based upon the average execution time of solution.pyz.

## Execution
In order to run the evaluation script we will be running use `./evaluation.bash` this will produce an output file with the scoring metrics.

In order to only test the dice coefficient of individual images one can run:
`python3.6 main.py -i /path/to/segmentedimage -g /path/to/groundtruth`