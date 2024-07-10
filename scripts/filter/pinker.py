import numpy as np

def run_filter(image):
    blueness = 255 - image[:, :, 0]
    pink = np.stack([255 - blueness, np.zeros_like(blueness), 255 - blueness], axis=-1)
    image = pink.astype(np.uint8)

    return image