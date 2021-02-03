import cv2
import numpy as np
import imutils

# img = cv.imread('test.jpg')

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# mask = cv.inRange(hsv, (36, 25, 25), (70, 255,255))

# imask = mask > 0;
# green = np.zeros_like(img, np.uint8)
# green[imask] = img[imask]

# h, s, v1 = cv.split(green)

# treshold, tresh = cv.threshold(img, 150, 255, 0)
# contours,hierarchy = cv.findContours(treshold, 1, 2)

# ret,thresh = cv.threshold(img,127,255,0)
# contours,hierarchy = cv.findContours(thresh, 1, 2)

# cnt = contours[0]
# area = cv.contourArea(cnt)

# cv.imshow('contur', area)

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# # lower_green = np.array([36, 25, 25])
# # upper_green = np.array([70, 255,255])

# mask = cv.inRange(hsv, (36, 25, 25), (70, 255,255))

# cnts = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)

# for c in cnts: 
#     area = cv.contourArea(c)

#     cv.drawContours(img, [c], -1, (0, 0, 225), 1)

#     # M = cv.moments(c)

#     # cx = int(M["m10"] / M["m00"])
#     # cy = int(M["m01"] / M["m00"])

#     # cv.circle(img, (cx, cy), 7, (255,255,255), -1)
#     # cv.putText(img, "center", (cx-20, cy-20), cv.FRONT_HERSHEY_SIMPLEX, 0.5, (0,225, 0), 1)

# cv.imshow("test", img)
# cv.waitKey(0)

import cv2

# image = cv2.imread('test2.jpg')
# blur = cv2.medianBlur(image, 9)
# # gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray, 127 ,255, cv2.THRESH_BINARY_INV)[1]

# cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# min_area = 5000
# for c in cnts:
#     area = cv2.contourArea(c)
#     if area > min_area:
#         cv2.drawContours(image,[c], 0, (0,0,0), 2)

# # cv2.imshow('thresh', thresh)
# cv2.imshow('image', image)
# cv2.waitKey(0)

import cv2
import numpy as np
image = cv2.imread('test2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.imread('test2.jpg')
blur = cv2.medianBlur(image, 9)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 127 ,255, cv2.THRESH_BINARY_INV)[1]
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

min_area = 5000
for c in cnts:
    area = cv2.contourArea(c)
    if area > min_area:
        cv2.drawContours(image,[c], 0, (0,0,0), 2)

# cv2.imshow('thresh', thresh)
cv2.imshow('image', image)
cv2.waitKey(0)