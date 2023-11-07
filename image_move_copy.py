# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 07:10:46 2023


"""

import cv2
import os

images_path="D:/hack_playgrround/Dataset-20230210T062819Z-001/Dataset/SORDI_2022_h4006_fire extinguisher/images"
destination_folder="D:/hack_playgrround/Dataset-20230210T062819Z-001/Dataset4"
for image in os.listdir(images_path):
    img=cv2.imread(images_path+"/"+image)
    cv2.imwrite(destination_folder+"/i"+image,img)
    