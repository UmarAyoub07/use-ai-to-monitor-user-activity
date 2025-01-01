# Use AI to monitor user activity
This repository contains a Python script that makes use of a trained AI model to monitor user activity. The AI model is trained to recognize different activities based on screenshots of the user's screen. The script takes a screenshot and then uses the model to predict the user's activity.

## Installation
The script requires the following Python libraries:
- keras
- PIL
- pyautogui
- numpy

You can install these using pip:
```
pip install keras pillow pyautogui numpy
```
You also need to have a trained model. The script expects a keras model named 'activity_model.h5' in the same directory.

## Usage
To run the script, navigate to the directory containing the script and the model, then run:
```
python monitor_activity.py
```
The script will start monitoring user activity, printing the predicted activity to the console.

## Warning
This script should only be used for legitimate purposes, such as studying your own activity or for research purposes. Unauthorized monitoring of other people's activity is a violation of privacy.