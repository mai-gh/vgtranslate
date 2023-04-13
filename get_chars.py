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

gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)



#data = pytesseract.image_to_string(gray, lang='jpn', config='--psm 6').lower() 
#data = pytesseract.image_to_data(gray, lang='jpn', config='--psm 6', output_type=Output.DICT)
data = pytesseract.image_to_data(gray, lang='jpn', config='--psm 6')




#print(json.dumps(data, indent=2))
print(data)
