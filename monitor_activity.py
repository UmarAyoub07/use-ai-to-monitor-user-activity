# Import necessary libraries
from pyautogui import screenshot
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

# Load the trained model
model = load_model('activity_model.h5')

# Function to predict user activity
def predict_activity():
    # Take a screenshot
    img = screenshot()

    # Preprocess the image
    img = img.resize((64, 64))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)

    # Predict the activity
    activity = model.predict_classes(img)

    return activity

# Monitor user activity
while True:
    activity = predict_activity()
    print(f'User activity: {activity}')