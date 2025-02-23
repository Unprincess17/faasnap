#!/bin/bash
sudo apt install -y redis-server ffmpeg        && \
sudo pip install redis flask pillow ffmpeg chameleon igraph  && \
# compatible with python 3.8 and suitable for no-gpu and limited memory environment
sudo pip install torch==1.9.1+cpu torchvision==0.10.1+cpu torchaudio==0.9.1 --index-url https://download.pytorch.org/whl/cpu && \

sudo redis-cli CONFIG SET requirepass "123456" && \
sudo systemctl restart redis            && \

python populate_resource.py             