# -*- coding: utf-8 -*-
"""

@author: arun1
"""

import json
import os


def convert_to_labelme_format(annotations,i):
    labelme_annotations = []
    for annotation in annotations:
        labelme_annotation = {
            "shape_type": "rectangle",
            "label": annotation["ObjectClassName"],
            "points": [[annotation["Left"], annotation["Top"]], [annotation["Right"], annotation["Bottom"]]],           
            "group_id": annotation["ObjectClassId"],
            "flags": {}
        }
        labelme_annotations.append(labelme_annotation)

    labelme_format = {
        "version": "5.0.1",
        "flags": {},
        "shapes": labelme_annotations,
        "imagePath": i[:-4]+"jpg",
        "imageData": "null",
        "imageHeight": "720",
        "imageWidth": "1280"
    }

    return labelme_format

def file_loader(path,new_path):
    for i in os.listdir(path):
        with open(path+"/"+i) as json_file:
            annotations=json.load(json_file)
            labelme_format = convert_to_labelme_format(annotations,i)
            json_file.close()
        with open(new_path+"/"+i[:-4]+"json","a+") as outfile:
            json.dump(labelme_format,outfile,indent=2)
            outfile.close()

path="D:/hack_playgrround/Dataset-20230210T062819Z-001/Dataset/SORDI_2022_h4005_exit sign/labels"
new_folder="D:/d1"
file_loader(path,new_folder)
