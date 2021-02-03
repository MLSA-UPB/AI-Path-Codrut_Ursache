'''
TODOS
1. resizing image
2. bgr-> hsv
3. color filers (B, G, R)
4. find contours
'''
import cv2
import numpy as np
import imutils
from numpy.lib.shape_base import column_stack

img = cv2.imread('alin.png')
# cv2.imshow("test", img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# blue range
lower_blue = np.array([90,60,0])
upper_blue = np.array([121, 225,255])

# green range
lower_green = np.array([36, 25, 25])
upper_green = np.array([70, 255,255])

# red range
lower_red = np.array([170, 70, 50])
upper_red = np.array([180, 255, 255])

mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_red = cv2.inRange(hsv, lower_red, upper_red)

blue_contours = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
blue_contours = imutils.grab_contours(blue_contours)

green_contours = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
green_contours = imutils.grab_contours(green_contours)

red_contours = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
red_contours = imutils.grab_contours(red_contours)

for cb in blue_contours:
    # area = cv2.contourArea(cb)
    # if area > 500: 
    #    cv2.drawContours(img, [cb], -1, (0,0,0), 3)
    # divs = np.array()
    x,y,w,h = cv2.boundingRect(cb)
    divs = np.array([x, y, w, h])
    cv2.rectangle(img, (x, y), (x+w, y+h), (225, 255, 0), 2)
    print('divs: ', divs)

for cg in green_contours:
    # area = cv2.contourArea(cb)
    # if area > 500: 
    #    cv2.drawContours(img, [cb], -1, (0,0,0), 3)
    # divs = np.array()
    x,y,w,h = cv2.boundingRect(cg)
    paragraphs = np.array([x, y, w, h])
    cv2.rectangle(img, (x, y), (x+w, y+h), (225, 225, 0), 2)
    print('paragraphs: ', paragraphs)

for cr in red_contours:
    # area = cv2.contourArea(cb)
    # if area > 500: 
    #    cv2.drawContours(img, [cb], -1, (0,0,0), 3)
    # divs = np.array()
    x,y,w,h = cv2.boundingRect(cr)
    images = np.array([x, y, w, h])
    cv2.rectangle(img, (x, y), (x+w, y+h), (225, 225, 0), 2)
    print('images: ',images)

cv2.imshow("test", img)
cv2.waitKey(0)