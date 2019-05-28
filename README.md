# Server-temp

## About

This system uses Computer Vision to detect the temperature reading from the display and sends out alerts accordingly. This repository is where you can find the code that does the same.

### Requirements:
* Python 3.x
* Installing OpenCV on Raspberry Pi:
    - Refer to [this guide](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi), if necessary, to install OpenCV on your Pi.

### Getting Started

* Register
    A site for users to register by providing a temperature threshold and email/phone number to receive alerts is up and running at :
    ``` [Site] (https://roomserver.github.io/Server-Temperature/) ```
    Users can opt-out from or resume receiving notifications via sending a mail by clicking on the link available on the site.
    
* Accessing the Raspberry Pi camera with Python and OpenCV:
    A picture of the temperature display is to be taken to be processed. A picture is taken every hour by setting up a cron job. This picture is saved to be processed only if the lights aren't turned on in the server room, i.e. only when the environment is dark.
    
###### Saving the image:
```python
# image is the opencv numpy array representation of the picture taken
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (5, 5))
if cv2.mean(blur)[0] < 3.0:
	cv2.imwrite('/home/pi/Pictures/server/image.jpg', image)
else:
	# Lights on
	pass
```

A sample image: 
![Temp display](/images/image.jpg)

Full Code on Github can be found [here](https://github.com/shwetha1607/Server-temp/blob/Version-1.1/stillpic.py)

* Detecting the temperature reading:


### References

* [Accessing Picamera with OpenCV and python](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/)
    

