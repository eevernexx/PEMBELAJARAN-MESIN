import os 
import pathlib 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

#walk through the directory and list the numbers of files=========================================================================================
for dirpath, dirnames, filenames in os.walk("/kaggle/input/nike-adidas-and-converse-imaged"):
  print(f"There are {len(dirnames)} directories and {len(filenames)} images in {dirpath}")

#Alternative way to see how many images we do have=========================================================================================
  num_nike_images_train = len(os.listdir("/kaggle/input/nike-adidas-and-converse-imaged/train/nike"))
num_nike_images_train

#Get the class names programatically=========================================================================================
data_dir = pathlib.Path("/kaggle/input/nike-adidas-and-converse-imaged/train")
class_names = np.array(sorted([item.name for item in data_dir.glob("*")])) # creating a list of class names from subdirectory 
print(class_names)

#Lets visualize the images=========================================================================================
def view_random_image(target_dir, target_class):
  # setting up the image directory
  target_folder = target_dir + target_class

  #get a random image path
  random_image = random.sample(os.listdir(target_folder), 1)

  #read image and plotting it
  img = mpimg.imread(target_folder + "/" + random_image[0] )
  plt.imshow(img)
  plt.title(target_class)
  plt.axis("off")

  print(f"Image shape: {img.shape}")
  
  return img