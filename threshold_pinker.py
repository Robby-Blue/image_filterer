import cv2
import numpy as np

def run_filter(image):
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    image[mask > 0] = [180, 50, 180]

    return image