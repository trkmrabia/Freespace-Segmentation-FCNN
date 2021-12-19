import os

# Path to jsons
JSON_DIR = 'C:/Users/rabia/Desktop/Freespace-Segmentation-with-FCNN-Intern/data/jsons'

# Path to mask
MASK_DIR  = 'C:/Users/rabia/Desktop/Freespace-Segmentation-with-FCNN-Intern/data/masks'
if not os.path.exists(MASK_DIR):
    os.mkdir(MASK_DIR)

# Path to output images
IMAGE_OUT_DIR = 'C:/Users/rabia/Desktop/Freespace-Segmentation-with-FCNN-Intern/data/masked_images'
if not os.path.exists(IMAGE_OUT_DIR):
    os.mkdir(IMAGE_OUT_DIR)

# Path to original images
IMAGE_DIR = 'C:/Users/rabia/Desktop/Freespace-Segmentation-with-FCNN-Intern/data/images'

MODEL_DIR  = 'C:/Users/rabia/Desktop/Freespace-Segmentation-with-FCNN-Intern/data/model'
if not os.path.exists(MASK_DIR):
    os.mkdir(MASK_DIR)

# In order to visualize masked-image(s), change "False" with "True"
VISUALIZE = True

# Bacth size
BACTH_SIZE = 4

# Input dimension
HEIGHT = 224
WIDTH = 224

# Number of class, for this task it is 2: Non-drivable area and Driviable area
N_CLASS= 2