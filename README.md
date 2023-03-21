# Preliminary Sample Solution for LPCVC 2023

> Example solution for [`LPCVC 2023`](http://lpcv.ai) for a linux based environment.
### We will be releasing a NVIDIA Jetpack tested solution soon.

## Table of Contents

- [Sample Solutions for LPCVC 2023](#sample-solutions-for-lpcvc-2023)
  - [Table of Contents](#table-of-contents)
  - [Dependencies](#dependencies)
  - [Evaluation](#evaluation)
    - [Format](#format)
    - [Submission](#submission)
    - [Metrics](#metrics)

## Dependencies

The evaluation of these sample models is dependent upon
[`Python 3.6.9`]

The following `Python 3.6.9` dependencies are necessary:

- `certifi==2021.5.30`
- `dataclasses==0.8`
- `imageio==2.15.0`
- `numpy==1.19.5`
- `opencv-python==4.7.0.72`
- `Pillow==8.4.0`
- `torchvision==0.11.2`
- `torch==1.10.1`
- `typing_extensions==4.1.1`

These dependencies are all that will be installed on the evaluation nanos.

It is recommended to create a conda environment for testing purposes. e.g. `conda create --name my_env python=3.6.9`

We provide a [`requirements.txt`](requirements.txt) file that can be used to
install the dependencies with the following commands:

1. `python3.6 -m pip install --upgrade pip`
1. `python3.6 -m pip install -r requirements.txt`

`pip list` should produce an output the same as below, where the packages not included with `requirements.txt` are default python packages:

```
Package           Version
----------------- ---------
certifi           2021.5.30
dataclasses       0.8
imageio           2.15.0
numpy             1.19.5
opencv-python     4.7.0.72
Pillow            8.4.0
pip               21.3.1
setuptools        58.0.4
torch             1.10.1
torchvision       0.11.2
typing_extensions 4.1.1
wheel             0.37.1
```

## Evaluation

### Format

- Input/output resolution: 512\*512
- Model Output: `14 * 512 * 512` for `Channel * Height * Width`. Each channel
  corresponds to the predicted probability for one category.

### Submission
- Each team should submit only one file, `solution.pyz`: the zipped package of solution/. [`zipapp`](https://docs.python.org/3/library/zipapp.html) should be used to compress the package.

Recommended command where solution is the name to your directory: `python3.6 -m zipapp  solution  -p='/usr/bin/env python3.6'`

### Metrics
- Accuracy: Dice Coefficient over all 14 categroies. As calculated in evaluation/Accuracy.py
- Speed: Average runtime for processing one frame (s/f). As calculated in evaluation/evaluation.bash

