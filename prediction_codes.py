# -*- coding: utf-8 -*-
"""

"""

import os
import torch
import xlwt
from xlwt import Workbook
import cv2
  

weights_path="D:/hack_playgrround/without_aug_test.pt"
weights_path="C:/Users/arun1/Downloads/exp/exp/weights/best.pt"   #location of weights
model=torch.hub.load('D:/git_repositories/yolov5','custom',weights_path,source='local')
model.conf=0.5
path="C:/Users/arun1/Downloads/im_test"   #images_folder
save_location="C:Users/arun1/Downloads/results_folder" #path to the result folder


wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
a=0
cell_index=0
files=os.listdir(path)
for i in files:
    p=path+"/"+i
    results=model(p)
    results.save(save_dir=save_location)
    if results.pred[0].shape[0]:
        df=(results.pandas().xyxy[0])
        count=len(df.index)
        print(count)
        sheet1.write_merge(cell_index,cell_index+count-1,0,0,i)
        sheet1.write_merge(cell_index,cell_index+count-1,1,1,count)
        cell_index=cell_index+count
        for j in range(count):
            confidence_list=df['confidence'][j]
            class_name=df['name'][j]
            sheet1.write(a,2,confidence_list)
            sheet1.write(a,3,class_name)           
            a=a+1            
wb.save(save_location+'/prediction_excel.xls')