# Sample Solution for LPCVC 2023

> An example solution for LPCVC 2023

## Table of Contents

- [Sample Solution for LPCVC 2023](#sample-solution-for-lpcvc-2023)
  - [Table of Contents](#table-of-contents)
  - [Dependencies](#dependencies)
  - [Testing Data](#testing-data)
  - [Evaluation](#evaluation)
    - [Format](#format)
    - [Metrics](#metrics)
  - [Submission](#submission)
    - [Sample-1](#sample-1)
    - [Sample-2 (We will provide this as the examplar solution)](#sample-2-we-will-provide-this-as-the-examplar-solution)

## Dependencies

The sample solution is dependent upon the following software:

- [`Python 3.10.9`](https://www.python.org/downloads/release/python-3109/)

The following Python packages are required to run the software:

- `imageio==2.15.0`
- `jetson_stats==3.0.1`
- `numpy==1.19.2`
- `torch==1.4.0`
- `torchvision==0.2.2.post3`
- `tqdm==4.64.1`

We provide a [`requirements.txt`](requirements.txt) file that can be used to
install the dependencies with the following commands:

1. `python3.10 -m pip install --upgrade pip`
1. `python3.10 -m pip install -r requriements.txt`
1. `sudo python3.10 -m pip install jetson-stats==3.0.1`

## Testing Data

- Download
  [testing data](https://drive.google.com/file/d/1cXHE2TKSqbl4u1haTGhBhwcUkt_RUhsl/view?usp=share_link)
  (Please keep this confidential and don't distribute)
- Organize testing directory as

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

- Accuracy: mIoU over all th 14 categories. By calling function `bench_acc()`.
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
