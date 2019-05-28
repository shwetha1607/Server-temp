# Server-temp

## About

This system uses Computer Vision to detect the temperature reading from the display and sends out alerts accordingly. This repository is where you can find the code that does the same.

### Requirements:
* Python 3.x
* Installing OpenCV on Raspberry Pi:
    - Refer to [this guide](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi), if necessary, to install OpenCV on your Pi. Once insalled correctly, you should be able to import it as:
    ```python
    import cv2
    ```

### Getting Started
    
* __*Accessing the Raspberry Pi camera with Python and OpenCV*__:
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

Full Code on Github: [stillpic.py](https://github.com/shwetha1607/Server-temp/blob/Version-1.1/stillpic.py)

* __*Detecting the temperature reading*__:
	The temperature reading is displayed as seven segment digits. The steps to detect what digit it reads are as follows:
	- Detecting the bright spots in the image: Thresholding operations followed by dilation, erosion and other preprocessing functions returns an image with only the digits displayed highlighted.
	- Extracting the digit ROI: Contours that are large enough to be a digit(the appropriate width and height constraints requires a few rounds of trial and error) in the image is taken as a digit ROI. A contour is simply a curve joining all the continuous points (along the boundary), having same color or intensity.
	- Identify the digits: Recognizing the actual digits with OpenCV will involve dividing the digit ROI into seven segments. From there, pixel counting on the thresholded image is applied to determine if a given segment is “on” or “off”.
	
Full Code on Github: [temp_detect.py](https://github.com/shwetha1607/Server-temp/blob/Version-1.1/temp_detect2.py)

* __*Register*__:
	A site for users to register by providing a temperature threshold and email/phone number to receive alerts is up and running at [this site] (https://roomserver.github.io/Server-Temperature/)
    
Users can opt-out from or resume receiving notifications via sending a mail with a specific subject and keyword by clicking on the link available on the site. Python's `imaplib` is used to read these received mails.
The database of users can be updated by running [getsheetdata.py](https://github.com/shwetha1607/Server-temp/blob/Version-1.1/getsheetdata.py). Google Drive and Sheets API and Python's `gspread` library is used to implement this. References to this is linked down below. The status of the user's notification preference( active or inactive) is also checked and updated in the process.

FUll code on Github: [getsheetdata.py](https://github.com/shwetha1607/Server-temp/blob/Version-1.1/getsheetdata.py), [receivemail.py](https://github.com/shwetha1607/Server-temp/blob/Version-1.1/receivemail.py)

* __*Mailing service for sending out alerts*__: 


### References

* [Accessing Picamera with OpenCV and python](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/)
* [Recognizing digits](https://www.pyimagesearch.com/2017/02/13/recognizing-digits-with-opencv-and-python/)
* [Google Spreadsheets and Python](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)
* [Python's imaplib](https://docs.python.org/3/library/imaplib.html)
