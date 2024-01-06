import tensorflow as tf
import pandas as pd;
import numpy
from PIL import Image
import os


#Get file path by joining path of program to relative path of images folder, then get names of images
file_name = os.path.join(os.path.dirname(__file__), 'frames')
try:
    image_names = os.listdir(file_name)
except FileNotFoundError:
    raise Exception("frames folder could not be found.")
if(len(image_names) == 0):
    raise Exception("No images provided in /frames")


#Initialize numpy arrays for data and labels, using the dimensions of the first image
first_img = numpy.array(Image.open("frames\\" + image_names[0]))
data = numpy.zeros(shape=(len(image_names), first_img.shape[0], first_img.shape[1]))
labels = numpy.zeros(shape=(len(image_names)))


#Open each image in grayscale and place in numpy array
i = 0
for name in image_names:
    img = (Image.open("frames\\" + name)).convert(mode="L")
    np_img = numpy.array(img)
    img.close()
    data[i] = np_img
    labels[i] = ("unproductive" in name)
    i += 1
    print(i)

    
print(np_img)
print(name)
print(data[0])
print(labels[0])


#Create model

#Train and save








