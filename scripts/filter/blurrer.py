import cv2
import numpy as np

def run_filter(image):
    blurred = cv2.GaussianBlur(image, (161, 161), 0)

    return blurred