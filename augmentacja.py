import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import imageio
import glob
import shutil

#augment the photo

ia.seed(10)

path = 'C:\\Users\\jerzy\\Desktop\\YOLO\\do_augmentacji\\'
files = glob.glob(path+"*.jpg")

for file in files:
    img = imageio.imread(file)
    images = np.array([img for _ in range(1)], dtype=np.uint8)
    seq = iaa.Sequential([
    iaa.Fliplr(0.5),
        iaa.Crop(percent=(0, 0.1)),
        iaa.Sometimes(
    0.5,
            iaa.GaussianBlur(sigma=(0, 0.5))
        ),
        iaa.LinearContrast((0.75, 1.5)),
        iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
        iaa.Multiply((0.8, 1.2), per_channel=0.2),
        iaa.Affine(
            scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
            translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
            rotate=(-25, 25),
            shear=(-8, 8)
        )
    ], random_order=True)

    images_aug = seq.augment_images(images)

    for i in range(1):
        imageio.imwrite(file.replace(".", "_new_"+str(i)+"."), images_aug[i])  #write all changed images
        shutil.copy(file.replace(".jpg", ".txt"), file.replace(".jpg", "_new_"+str(i)+".txt"))


