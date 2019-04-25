from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2

camera= PiCamera()
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera, size=(640,480))

time.sleep(5)
#camera.capture('/home/pi/Desktop/image.jpg')
camera.capture(rawCapture,format='bgr')
image = rawCapture.array

#at_time = time.strftime("%d%m%Y-%H%M%S", time.localtime())
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (5, 5))

if cv2.mean(blur)[0] < 3.0:
	cv2.imwrite('/home/pi/Pictures/server/image.jpg', image)
else:
	#print('lights on')
	pass