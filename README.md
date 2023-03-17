# Sample Solution for LPCVC 2023

> Example solution for LPCVC 2023

## Table of Contents

- [Sample Solutions for LPCVC 2023](#sample-solutions-for-lpcvc-2023)
  - [Table of Contents](#table-of-contents)
  - [How to Run](#how-to-run)
    - [Dependencies](#dependencies)
    - [Testing Dataset](#testing-dataset)
      - [Evaluation Directory Structure](#evaluation-directory-structure)
  - [Evaluation](#evaluation)
    - [Format](#format)
    - [Metrics](#metrics)

## How to Run

The following sections cover how to evaluate the sample solutions.

### Dependencies

he evaluation of these sample models is dependent upon
[`Python 3.6`](https://www.python.org/downloads/release/python-3109/)

The following `Python 3.6` dependencies are necessary:

- `certifi==2021.5.30`
- `dataclasses==0.8`
- `imageio==2.15.0`
- `numpy==1.19.5`
- `opencv-python==4.7.0.72`
- `Pillow==8.4.0`
- `torch==1.10.1`
- `torchvision==0.11.2`
- `typing_extensions==4.1.1`

These dependencies are all that will be installed on the evaluation nanos.

We provide a [`requirements.txt`](requirements.txt) file that can be used to
install the dependencies with the following commands:

1. `python3.10 -m pip install --upgrade pip`
1. `python3.10 -m pip install -r requirements.txt`
1. `sudo python3.10 -m pip install jetson-stats==3.0.1`

<!--### Testing Dataset

Please do not distribute the testing data.

- [Download the testing data](https://drive.google.com/file/d/1cXHE2TKSqbl4u1haTGhBhwcUkt_RUhsl/view?usp=share_link)

#### Evaluation Directory Structure

This evaluation is dependent upon the following directory structure:

1. Extract the `LPCVC_Test\IMG` and `LPCVC_Test\GT` folders from the testing
   data zip file.
1. Move these directories to the [`data`](data/) directory

The desired directory structure is the following:

```shell
├── util
|── README.md
|── submission1
|── submission1.py
|── submission2
|── submission2.py
└── data
    └── .gitkeep
    └── IMG
        ├── test_0000.png
        ├── test_0001.png
        ├── ...
        └── test_0599.png
    └── GT
        ├── test_0000.png
        ├── test_0001.png
        ├── ...
        └── test_0599.png
```
-->
## Evaluation

### Format

- Input/output resolution: 512\*512
- Model Output: `14 * 512 * 512` for `Channel * Height * Width`. Each channel
  corresponds to the predicted probability for one category.

## Submission
- Each team should submit only one file, `solution.pyz`: the zipped package of solution/. [`zipapp`](https://docs.python.org/3/library/zipapp.html) should be used to compress the package.

### Metrics

- Accuracy: Dice Coefficient over all 14 categroies. As calculated in evaluation/Accuracy.py
- Speed: Average runtime for processing one frame (s/f). As calculated in evaluation/evaluation.bash

<!-- - Accuracy: mIoU over all the 14 categories. By calling function `bench_acc()`.
- Speed: average runtime for processing one frame (s/f). By calling function
  `bench_speed()`.
- Power: power consumption of GPU for processing one frame (mJ/f). By calling
  function `bench_power()`. -->

<!-- ## Submission

> NOTE: These are subject to change prior to the competition starting

For a submission *MODEL*, there are should be

- *MODEL.py*: a formatted file for performing evaluation
- *MODEL*: a folder containing related model files, weights, etc. -->

<!--### Sample 1

- Run `python submission1.py`
- `submission1` is plain pytorch model-->

<!-- ### Sample-2 (We will provide this as the exemplar solution)

- Run `python submission2.py`
- `submission2` is tenorRT model converted from Sample-1. -->
