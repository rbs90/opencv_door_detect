import cv2
from numpy import *

test_imgs = ['night_open.jpg', 'night_closed.jpg', 'day_open.jpg', 'day_closed.jpg']

for imgFile in test_imgs:
	img = cv2.imread(imgFile)
	height, width, channels = img.shape
	mask = zeros((height+2, width+2), uint8)

	#the starting pixel for the floodFill
	start_pixel = (510,110)
	#maximum distance to start pixel:
	diff = (2,2,2)

	retval, rect = cv2.floodFill(img, mask, start_pixel, (0,255,0), diff, diff)

	print retval

	#check the size of the floodfilled area, if its large the door is closed:
	if retval > 10000:
		print imgFile + ": garage door closed"
	else:
		print imgFile + ": garage door open"

	cv2.imwrite(imgFile.replace(".jpg", "") + "_result.jpg", img)	


'''
img = cv2.resize(img,(400,500))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,gray = cv2.threshold(gray,127,255,0)
gray2 = gray.copy()
mask = cv2.cvtColor(gray2, cv2.COLOR_GRAY2RGB)

contours, hier = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
	if 100<cv2.contourArea(cnt)<5000:
		cv2.drawContours(mask, [cnt], 0, (0,255, 0), 2);
    
	#if 200<cv2.contourArea(cnt)<5000:
    #    (x,y,w,h) = cv2.boundingRect(cnt)
    #    cv2.rectangle(mask,(x,y),(x+w,y+h), ( 0, 255, 0))



#cv2.rectangle(mask,(20,20),(40,40), ( 0, 255, 0))

cv2.imshow('IMG',gray)
cv2.imshow('IMG',gray2)
cv2.imshow('IMG',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
