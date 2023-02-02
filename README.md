# Sample Solutions for LPCVC 2023

> Example solutions for LPCVC 2023

## Table of Contents

- [Sample Solutions for LPCVC 2023](#sample-solutions-for-lpcvc-2023)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How to Run](#how-to-run)
    - [Dependencies](#dependencies)
    - [Testing Dataset](#testing-dataset)
      - [Evaluation Directory Structure](#evaluation-directory-structure)
  - [Evaluation](#evaluation)
    - [Format](#format)
    - [Metrics](#metrics)
  - [Submission](#submission)
    - [Sample-1](#sample-1)
    - [Sample-2 (We will provide this as the examplar solution)](#sample-2-we-will-provide-this-as-the-examplar-solution)

## About

This repository contains sample solutions for the 2023 Low Powered Computer
Vision Challenge (LPCVC) and the training code to generate the solutions.

This repository has two branches:

1. `main` (this branch): Contains the testing and evaluation of the sample
   solutions
1. `training`: Contains training code that was used to generate the sample
   solutions

The remainder of this `README.md` will cover content specific to the `main`
branch. For information on how to run the training examples, please see the
`training` branch's `README.md`.

## How to Run

The following sections cover how to evaluate the sample solutions.

### Dependencies

The evaluation of these sample models is dependent upon
[`Python 3.10`](https://www.python.org/downloads/release/python-3109/)

The following `Python 3.10` dependencies are necessary for evaluation:

- `imageio`
- `jetson_stats`
- `numpy`
- `torch`
- `torchvision`
- `tqdm`

We provide a [`requirements.txt`](requirements.txt) file that can be used to
install the dependencies with the following commands:

1. `python3.10 -m pip install --upgrade pip`
1. `python3.10 -m pip install -r requriements.txt`
1. `sudo python3.10 -m pip install jetson-stats==3.0.1`

### Testing Dataset

Please do not distribute the testing data following testing data.

- [Download the testing data](https://drive.google.com/file/d/1cXHE2TKSqbl4u1haTGhBhwcUkt_RUhsl/view?usp=share_link)

#### Evaluation Directory Structure

Plese store the testing data in this repositories [`data`](data/) directory.

The desired directory structure is the following:

```shell
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
        └── test_0599.png
    └── GT
        ├── test_0000.png
        ├── test_0001.png
        ├── ...
        └── test_0599.png
```

## Evaluation

### Format

- Input/output resolution: 512\*512
- Model Output: `14 * 512 * 512` for `Channel * Height * Width`. Each channel
  corresponds to the predicted probability for one category.

### Metrics

- Accuracy: mIoU over all the 14 categories. By calling function `bench_acc()`.
- Speed: average runtime for processing one frame (s/f). By calling function
  `bench_speed()`.
- Power: power consumption of GPU for processing one frame (mJ/f). By calling
  function `bench_power()`.

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
