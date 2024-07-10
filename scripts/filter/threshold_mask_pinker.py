import numpy as np

def run_filter(r):
    image, mask = r

    m_height, m_width, _ = mask.shape
    height, width, _ = image.shape

    mask_x = np.repeat(np.arange(width) * m_width // width, height).reshape(width, height).T
    mask_y = np.repeat(np.arange(height) * m_height // height, width).reshape(height, width)

    mask_indices = (mask_y, mask_x)
    blueness = image[:, :, 0]
    blue_mask = blueness > 140
    pink = mask[mask_indices]

    image[blue_mask] = pink[blue_mask]

    return image
