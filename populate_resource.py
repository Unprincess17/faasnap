import redis
import os

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password="123456") 
# r.flushdb() # flushes the current database
# # image_dir = '/home/pxg/faasnap/resources/image'
data =[]
data.append(['/mnt/data/faasnap/resources/image','.jpg'])
data.append(['/mnt/data/faasnap/resources/image','.jpeg'])
data.append(['/mnt/data/faasnap/resources/json','.json'])
data.append(['/mnt/data/faasnap/resources/ffmpeg','.mp4'])
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
os.chdir('/mnt/data/faasnap/')
os.makedirs('resources/recognition', exist_ok=True)
with open('resources/recognition/resnet50.pth', 'wb') as f:
  f.write(response.content)
  
# Load model into Redis
# with open('/mnt/data/faasnap/resources/recognition/resnet50.pth', 'rb') as f:
#   model_data = f.read()
#   r.set('resnet50.pth', model_data)

with open('/mnt/data/faasnap/resources/recognition/resnet50-19c8e357.pth', 'rb') as f:
  model_data = f.read()
  r.set('resnet50-19c8e357.pth', model_data)

# print(r.get('resnet50.pth')[:50]) # print first 50 bytes to verify 
print(r.keys()) 
