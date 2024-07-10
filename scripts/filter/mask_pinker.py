import numpy as np

def run_filter(r):
    image, mask = r

    m_height, m_width, _ = mask.shape
    height, width, _ = image.shape

    mask_x = (np.arange(width) * m_width / width).astype(int)
    mask_y = (np.arange(height) * m_height / height).astype(int)
    
    mask_coords_x, mask_coords_y = np.meshgrid(mask_x, mask_y)
    m_pixel = mask[mask_coords_y, mask_coords_x]
    blueness = image[:, :, 0].astype(float) / 255
    pink = m_pixel * blueness[:, :, np.newaxis]
    image[:, :] = pink.astype(np.uint8)
    
    return image