import shutil
import numpy as np
import cv2 as cv
import glob

def is_jpg(filename):
	if filename[-3:] == 'jpg':
		return True
	else:
		return False

def is_txt(filename):
	if filename[-3:] == 'txt':
		return True
	else:
		return False

def adjust_gamma(image, gamma=1.0):
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	return cv.LUT(image, table)

# path_to_originals = "C:\\Users\\jerzy\\Desktop\\YOLO\\super_dataset\\"
path_to_originals = "C:\\Users\\jerzy\\Desktop\\YOLO\\DoorDetect-Dataset-master\\images\\"
# path_to_originals = "C:\\Users\\jerzy\\Desktop\\YOLO\\zdjecia\\"
path_to_corrected = "C:\\Users\\jerzy\\Desktop\\YOLO\\DoorDetect-Dataset-master\\images_after\\"

#lista pelnych sciezek
list_of_jpgs = filter(is_jpg, glob.glob(path_to_originals + "*"))
list_of_txts = filter(is_txt, glob.glob(path_to_originals + "*"))

txt_flag = 1

for file in list_of_jpgs:
	print(file)
	nazwa_pliku = file.split('\\')[-1]
	img = cv.imread(file, 0)
	modified = cv.Canny(img,100,200)
	cv.imwrite(path_to_corrected+nazwa_pliku, modified)
if txt_flag:
	for file in list_of_txts:
		nazwa_pliku = file.split('\\')[-1]
		shutil.copy(file, path_to_corrected+nazwa_pliku)
