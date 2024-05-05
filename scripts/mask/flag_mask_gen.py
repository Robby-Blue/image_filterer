import cv2
import numpy as np

def gen(colors):
    width = 144
    height = 256

    start_gay = 0
    end_gay = 256

    image = np.zeros((height, width, 3), np.uint8)

    rows_per_color = (end_gay - start_gay) // len(colors)+1

    for y in range(start_gay, end_gay):
        for x in range(width):
            color_idx = (y-start_gay)//rows_per_color
            color = colors[color_idx]
            image[y, x] = color

    for _ in range(15):
        image = cv2.GaussianBlur(image, (101, 101), cv2.BORDER_DEFAULT)
    
    return image