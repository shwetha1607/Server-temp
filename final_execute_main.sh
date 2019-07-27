#!/bin/bash

source /home/pi/.profile
workon cv
python /home/pi/stillpic.py

cd /home/pi/Pictures/"$(date +"%Y-%m-%d")"
mv test.wav  "$(date +"%T")".wav
cd /home/pi/Detect_Notify/
python /home/pi/Detect_Notify/main.py

