import glob
import cv2
import numpy as np
from shutil import copyfile

#check if a photo is bright or dark

path_to_images = 'C:\\Users\\jerzy\\Desktop\\YOLO\\super_dataset'
path_to_results = 'C:\\Users\\jerzy\\Desktop\\YOLO\\ciemne'

files = glob.glob(path_to_images+'\\'+'*.jpg')

def is_dark(image, dim=10, thresh=0.35):
    image = cv2.resize(image, (dim, dim))
    L, A, B = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2LAB))
    L = L/np.max(L)
    return np.mean(L) < thresh

for file in files:
	image = cv2.imread(file)
	if is_dark(image):
		print(file)
		copyfile(file, file.replace('super_dataset', 'ciemne'))
