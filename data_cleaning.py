# -*- coding: utf-8 -*-
"""

@author: arun1
"""

import os
import shutil
path="D:/hack_playgrround/Dataset-20230210T062819Z-001/Dataset4/fire_extinguisher"
imgs=[]
for img in os.listdir(path):
    imgs.append(img)
    
for label in os.listdir(path+"/"+"Annotations"):
    if label[:-4]+"jpg" in imgs:
        pass
    else:
        shutil.move(path+"/"+"Annotations/"+label,"D:/dummy/"+label)

