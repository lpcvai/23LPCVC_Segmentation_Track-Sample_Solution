# Sample Solution for LPCVC 2023

> Example solution for LPCVC 2023 for a Jetson Nano
# NOTICE Timing Change
> Participants will now be printing out their summed inference time in seconds as in solution/main.py.

## Table of Contents

- [Sample Solutions for LPCVC 2023](#sample-solutions-for-lpcvc-2023)
  - [Table of Contents](#table-of-contents)
  - [Setting Up Jetson Nano](#SetUp)
  - [Dependencies](#dependencies)
  - [Evaluation](#evaluation)
    - [Format](#format)
    - [Submission](#submission)
    - [Metrics](#metrics)
## SetUp
### Requirements
 - Computer or VM (recommend VMWare) running Desktop Image of [Ubuntu 18.04 x64](https://releases.ubuntu.com/18.04/)
 - [NVIDIA SDK Manager](https://developer.nvidia.com/sdk-manager)
 - jumper wire
 - USB-C 5V-3A Charger
 - ethernet
 - Micro SD (32 GB and larger)
 - Micro usb

## Installation
1. Insert Micro SD
2. Jump pins 9 and 10 (GND and FC REC) on J12
3. Plug in Micro usb connecting Nano and Computer
4. Plug in Ethernet
5. Plug in Power 
6. Using SDK Manager Flash Jetson Nano with jetPack 4.6.3 with NVIDIA DeepStream SDK selected as well
7. Follow instructions on SDK Manager
### Note
  - When trying to install the SDK components via the SDK Manager,you may get an error that the manager cannot connect to the device via ssh.
  To work around this:
  - Go to the downloads directory on your local computer and copy all of the sdk files to a USB drive
  - Open up the desktop on your jetson nano and install all of the software from the usb drive(may need to copy it to machine)
  - Some .deb files that install repositories. Those will display instructions to install GPG keys post installation
  - Additionally, we recommend installing the software in alphabetical order 3 times. Some of the software is dependent upon components that appear later in the        directory listing and we were unsure of the specific order.
  - To install you can run `sudo dpkg -i *.deb` this will install all deb files in a specified directory
  - Then run `sudo apt --fix-broken install -y` to fix any broken packages
### Dependencies

The evaluation of these sample models is dependent upon below packages
[`Python 3.6.9`]

If using the nvidia Jetson Nano we provide a [`setup.bash`](setup.bash) that will install all dependencies that are on our Nano.

If running with the Jetson Nano and you are getting "illegal instruction (core Dumped) try running export OPENBLAS_CORETYPE=ARMV8.

We provide a [`setup.bash`](setup.bash) file that can be used to

When executing on the Jetson Nano after running [`setup.bash`](setup.bash) many of the packages are due to the steps from https://qengineering.eu/install-pytorch-on-jetson-nano.html and are not listed in requirements.txt:
```
Package                       Version
----------------------------- -------------------
apturl                        0.5.2
asn1crypto                    0.24.0
beautifulsoup4                4.6.0
blinker                       1.4
Brlapi                        0.6.6
certifi                       2021.5.30
chardet                       3.0.4
click                         8.0.4
colorama                      0.3.7
cryptography                  2.1.4
cupshelpers                   1.0
cycler                        0.10.0
Cython                        0.29.34
dataclasses                   0.8
decorator                     4.1.2
defer                         1.0.6
distro-info                   0.18ubuntu0.18.04.1
feedparser                    5.2.1
filelock                      3.4.1
future                        0.18.3
gdown                         4.7.1
graphsurgeon                  0.4.5
html5lib                      0.999999999
httplib2                      0.9.2
idna                          2.6
imageio                       2.15.0
importlib-metadata            4.8.3
importlib-resources           5.4.0
Jetson.GPIO                   2.0.17
keyring                       10.6.0
keyrings.alt                  3.0
language-selector             0.1
launchpadlib                  1.10.6
lazr.restfulclient            0.13.5
lazr.uri                      1.0.3
louis                         3.5.0
lxml                          4.2.1
macaroonbakery                1.1.3
Mako                          1.0.7
MarkupSafe                    1.0
matplotlib                    2.1.1
mock                          5.0.2
numpy                         1.19.5
oauth                         1.0.1
oauthlib                      2.0.6
onboard                       1.4.1
opencv-python                 4.7.0.72
pandas                        0.22.0
pbr                           5.11.1
Pillow                        8.4.0
pip                           21.3.1
protobuf                      3.0.0
pycairo                       1.16.2
pycrypto                      2.6.1
pycups                        1.9.73
PyGObject                     3.26.1
PyJWT                         1.5.3
pymacaroons                   0.13.0
PyNaCl                        1.1.2
pyparsing                     2.2.0
pyRFC3339                     1.0
PySocks                       1.7.1
python-apt                    1.6.6
python-dateutil               2.6.1
python-debian                 0.1.32
pytz                          2018.3
pyxattr                       0.6.0
pyxdg                         0.25
PyYAML                        3.12
requests                      2.18.4
requests-unixsocket           0.1.5
scipy                         0.19.1
SecretStorage                 2.3.1
setuptools                    58.3.0
simplejson                    3.13.2
six                           1.11.0
ssh-import-id                 5.7
system-service                0.3
systemd-python                234
tensorrt                      8.2.1.9
testresources                 2.0.1
torch                         1.10.0a0+git36449ea
torchvision                   0.11.2
tqdm                          4.64.1
typing_extensions             4.1.1
ubuntu-advantage-tools        8001
ubuntu-drivers-common         0.0.0
uff                           0.6.9
unity-scope-calculator        0.1
unity-scope-chromiumbookmarks 0.1
unity-scope-colourlovers      0.1
unity-scope-devhelp           0.1
unity-scope-firefoxbookmarks  0.1
unity-scope-manpages          0.1
unity-scope-openclipart       0.1
unity-scope-texdoc            0.1
unity-scope-tomboy            0.1
unity-scope-virtualbox        0.1
unity-scope-yelp              0.1
unity-scope-zotero            0.1
urllib3                       1.22
urwid                         2.0.1
virtualenv                    15.1.0
wadllib                       1.3.2
webencodings                  0.5
wheel                         0.37.1
xkit                          0.0.0
youtube_dl                    2018.3.14
zipp                          3.6.0
zope.interface                4.3.2
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
- Speed: Average runtime for processing one frame (s/f). As calculated in solution/main.py

