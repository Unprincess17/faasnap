import redis
import os
import requests

CWD = os.getcwd()
r = redis.Redis(host='127.0.0.1', port=6379, db=0) 
# r.flushdb() # flushes the current database
# # image_dir = '/home/pxg/faasnap/resources/image'
data =[]
data.append([f'{CWD}/resources/image','.jpg'])
data.append([f'{CWD}/resources/image','.jpeg'])
data.append([f'{CWD}/resources/json','.json'])
data.append([f'{CWD}/resources/ffmpeg','.mp4'])
for i in data:
  for filename in os.listdir(i[0]):
    if filename.endswith(i[1]):
      image_path = os.path.join(i[0], filename)
      with open(image_path, 'rb') as f:
        image_data = f.read()
        r.set(filename, image_data)



# Download model
response = requests.get(url='https://raw.githubusercontent.com/fregu856/deeplabv3/master/pretrained_models/resnet/resnet50-19c8e357.pth')
# 97.8 MB
os.makedirs('resources/recognition', exist_ok=True)
with open('resources/recognition/resnet50-19c8e357.pth', 'wb') as f:
  f.write(response.content)

with open('resources/recognition/resnet50-19c8e357.pth', 'rb') as f:
  model_data = f.read()
  r.set('resnet50-19c8e357.pth', model_data)

print(r.keys()) 
