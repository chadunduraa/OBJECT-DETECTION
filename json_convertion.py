# -*- coding: utf-8 -*-
"""

@author: arun1
"""
import os
import json

path="D:/hack_playgrround/Dataset-20230210T062819Z-001/Dataset3/fire_extinguisher"
new_folder="D:/hack_playgrround/Dataset-20230210T062819Z-001/Dataset4"
for file in os.listdir(path):
    with open(path+"/"+file) as file_opened:
        annotations=json.load(file_opened)
        temp_name=annotations["imagePath"]
        annotations["imagePath"]="i"+temp_name
    with open(new_folder+"/i"+file,"a+") as outfile:
        json.dump(annotations,outfile)
    