import numpy as np
import cv2
import json
import os
import torch
import tqdm 
from matplotlib import pyplot as plt
from skimage.transform import rotate, AffineTransform, warp
from skimage.util import random_noise
from skimage import transform
import random 
from torchvision import transforms as T
from PIL import Image

IMAGE_DIR='C:/Users/rabia/Desktop/Freespace-Segmentation-with-FCNN-Intern/data/images'

MASK_DIR='C:/Users/rabia/Desktop/Freespace-Segmentation-with-FCNN-Intern/data/masks'


#The path to the masks folder is assigned to the variable
image_path=[] #empty list created
for name in os.listdir(IMAGE_DIR):
    image_path.append(os.path.join(IMAGE_DIR,name))
mask_path=[] #empty list created


for name in os.listdir(MASK_DIR):
    mask_path.append(os.path.join(MASK_DIR,name))

valid_size = 0.3
test_size  = 0.1
indices = np.random.permutation(len(image_path))
test_ind  = int(len(indices) * test_size)
valid_ind = int(test_ind + len(indices) * valid_size)
train_input_path_list = image_path[valid_ind:]
train_label_path_list = mask_path[valid_ind:]

for image in tqdm.tqdm(train_input_path_list):
    img=Image.open(image)
    color_aug = T.ColorJitter(brightness=0.4, contrast=0.4, hue=0.06)

    img_aug = color_aug(img)
    new_path=image[:-4]+"-1"+".png"
    new_path=new_path.replace('image', 'augmentation')
    img_aug=np.array(img_aug)
    cv2.imwrite(new_path,img_aug)
    
    
  
    
for mask in tqdm.tqdm(train_label_path_list):
    msk=cv2.imread(mask)
    new_mask=msk
    newm_path=mask[:-4]+"-1"+".png"
    newm_path=newm_path.replace('masks', 'augmentation_mask')
    cv2.imwrite(newm_path,new_mask)
   
    
    
    