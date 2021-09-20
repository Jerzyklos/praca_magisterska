import numpy as np
import cv2 as cv
import glob

#adjust gamma of a photo

def adjust_gamma(image, gamma=1.0):
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	return cv.LUT(image, table)

path_to_originals = "C:\\Users\\jerzy\\Desktop\\YOLO\\ciemne\\"
path_to_corrected = "C:\\Users\\jerzy\\Desktop\\YOLO\\ciemne\\rozjasnione\\"

list_of_jpgs = glob.glob(path_to_originals+'*jpg')

gamma = 1.5

for file in list_of_jpgs:
    original = cv.imread(file)
    nazwa_pliku = file.split('\\')[-1]
    adjusted = adjust_gamma(original, gamma=gamma)
    cv.imwrite(path_to_corrected+nazwa_pliku, adjusted)
