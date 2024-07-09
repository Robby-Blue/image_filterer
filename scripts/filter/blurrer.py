import cv2

def run_filter(image):
    blurred = cv2.GaussianBlur(image, (51, 51), 0)

    return blurred