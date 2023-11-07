# -*- coding: utf-8 -*-
"""


"""

import os
import cv2
import sys
import torch

path="D:/hack_playgrround/without_aug_test.pt"
model=torch.hub.load('D:/git_repositories/yolov5','custom',path,source='local')
vid = cv2.VideoCapture(0)#,cv2.CAP_DSHOW)
while(vid.isOpened()):
    frame1,frame2=vid.read()
    results=model(frame2)
    qr=results.render()               
    cv2.imshow("live_feed",qr[0])
    if cv2.waitKey(1) & 0xFF in (ord('q'), 27):
        break
vid.release()
cv2.destroyAllWindows()



