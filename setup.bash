#!/bin/bash

sudo apt --fix-broken install -y
sudo apt update
sudo apt upgrade -y
sudo apt install software-properties-common -y
sudo apt autoremove --purge -y
sudo apt --fix-broken install -y

sudo apt install python3-pip -y
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

#If using Jetson Nano
#From https://qengineering.eu/install-pytorch-on-jetson-nano.html 
# Install the dependencies
pip uninstall torch
sudo apt-get install python3-pip libjpeg-dev libopenblas-dev libopenmpi-dev libomp-dev
pip install future
sudo pip3 install -U --user wheel mock pillow
pip install testresources
# Above 58.3.0 you get version issues
pip install setuptools==58.3.0
pip install Cython
# Install gdown to download from Google Drive
pip install gdown
# Download the wheel
gdown https://drive.google.com/uc?id=1TqC6_2cwqiYacjoLhLgrZoap6-sVL2sd
# Install PyTorch 1.10.0
pip install torch-1.10.0a0+git36449ea-cp36-cp36m-linux_aarch64.whl
# Clean up
rm torch-1.10.0a0+git36449ea-cp36-cp36m-linux_aarch64.whl

sudo apt update
# Set OPENBLAS_CORETYPE=ARMV8
echo "export OPENBLAS_CORETYPE=ARMV8" >> ~/.bashrc
source ~/.bashrc

# Set power state of devices
sudo nvpmodel -m 1
