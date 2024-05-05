import scripts.mask.flag_mask_gen as mask

def run_filter(image):
    return image, mask.gen((
        (250, 206, 91),
        (184, 169, 245),
        (255, 255, 255),
        (184, 169, 245),
        (250, 206, 91),
    ))