#!/usr/bin/env python3

from PIL import Image
import cv2
import pytesseract
import numpy as np
from pytesseract import Output
import json


#frame = Image.open('./in.png').convert("L") # grayscale
frame = Image.open('./in.png') # grayscale
cv2_img = np.array(frame)
cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)

#gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)

#img = cv2.medianBlur(img,5)

#ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,th1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#            cv2.THRESH_BINARY,11,2)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#            cv2.THRESH_BINARY,11,2)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dilation = cv2.dilate(th1,kernel,iterations = 4)

#contours, _ = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#print(contours)

cnts = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]


ROI_number = 0
for c in cnts:
  area = cv2.contourArea(c)
  if area > 10000:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 3)
    ROI = img[y:y+h, x:x+w]
    cv2.imshow('cv2',ROI)
    

#for c in contours:
#  x,y,w,h = cv2.boundingRect(c)
#  cv2.rectangle(cv2_img,(x,y),(x+w,y+h),(255,0,0))



#ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
#rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (16, 16))
#dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
#contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
#                                                 cv2.CHAIN_APPROX_NONE)

#im2 = cv2_img.copy()
#for cnt in contours:
#  x, y, w, h = cv2.boundingRect(cnt)
#  rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
#  cropped = im2[y:y + h, x:x + w]
#  text = pytesseract.image_to_string(cropped, lang='jpn', config='--psm 6')
#  print("---------------------")
#  print("text: ", text)
#  print("---------------------")


#cv2.imshow('cv2',img)
#cv2.imshow('cv2',cv2_img)
#cv2.imshow('cv2',cv2_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




#data = pytesseract.image_to_string(gray, lang='jpn', config='--psm 6').lower() 
#data = pytesseract.image_to_data(gray, lang='jpn', config='--psm 6', output_type=Output.DICT)



#data = pytesseract.image_to_data(gray, lang='jpn', config='--psm 6')




#print(json.dumps(data, indent=2))
data = pytesseract.image_to_string(ROI, lang='jpn', config='--psm 6').lower() 

print(data)
