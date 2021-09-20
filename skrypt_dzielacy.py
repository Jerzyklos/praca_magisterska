import glob
import os
import shutil 
import random

ratio_validation = 0.15
ratio_testing = 0.10
train_dest = "C:\\Users\\jerzy\\Desktop\\YOLO\\train"
validation_dest = "C:\\Users\\jerzy\\Desktop\\YOLO\\validation"
testing_dest = "C:\\Users\\jerzy\\Desktop\\YOLO\\testing"
# files_location = "C:\\Users\\jerzy\\Desktop\\YOLO\\zdjecia_canny"

path = 'C:\\Users\\jerzy\\Desktop\\YOLO\\super_dataset\\'

list_of_files = glob.glob("C:\\Users\\jerzy\\Desktop\\YOLO\\super_dataset\\*.txt")
# list_of_files = glob.glob("C:\\Users\\jerzy\\Desktop\\YOLO\\zdjecia_canny\\*.txt")
names = [file.split("\\")[-1][:-4] for file in list_of_files]
how_many_validation = int(len(names) * ratio_validation)
how_many_testing = int(len(names) * ratio_testing)

files_to_copy_validation = []
for i in range(how_many_validation):
    file = random.choice(names)
    while file in files_to_copy_validation:
        file = random.choice(names)
    files_to_copy_validation.append(file)

files_to_copy_testing = []
for i in range(how_many_testing):
    file = random.choice(names)
    while file in files_to_copy_validation or file in files_to_copy_testing:
        file = random.choice(names)
    files_to_copy_testing.append(file)

files_to_copy_training = []
for name in names:
    if name not in files_to_copy_validation and name not in files_to_copy_testing:
        files_to_copy_training.append(name)
    
for file in files_to_copy_validation:
    shutil.copy(path+"\\"+file+".txt", validation_dest)
    shutil.copy(path+"\\"+file+".jpg", validation_dest)
for file in files_to_copy_training:
    shutil.copy(path+"\\"+file+".txt", train_dest)
    shutil.copy(path+"\\"+file+".jpg", train_dest)
for file in files_to_copy_testing:
    shutil.copy(path+"\\"+file+".txt", testing_dest)
    shutil.copy(path+"\\"+file+".jpg", testing_dest)

