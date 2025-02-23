# FaaSnapBench

This repo includes the benchmark used in paper:

Lixiang Ao, George Porter, and Geoffrey M. Voelker. 2022. [FaaSnap: FaaS Made Fast Using Snapshot-based VMs.](https://doi.org/10.1145/3492321.3524270) In Seventeenth European Conference on Computer Systems (EuroSys ’22), April 5–8, 2022, RENNES, France. ACM, New York, NY, USA, 17 pages. 




# Setup
Use `setup.sh` to make life easier :)

## Prepare input data
Download ResNet model [resnet50-19c8e357.pth](https://github.com/fregu856/deeplabv3/blob/master/pretrained_models/resnet/resnet50-19c8e357.pth) to `resources/recognition`.
## Setup redis
2. Start a local Redis instance on the default port 6379.
```
sudo apt install -y redis-server
sudo pip install redis

sudo redis-cli CONFIG SET requirepass "123456"
sudo systemctl restart redis
```
## Populate Redis
Populate Redis with files in `resources` directory and its subdirectory. The keys should be the last parts of filenames (`basename`).
```
python populate_resource.py
```
