import scripts.mask.flag_mask_gen as mask

def run_filter(image):
    return image, mask.gen((
        (3, 3, 228),
        (0, 140, 255),
        (0, 237, 255),
        (38, 128, 0),
        (142, 64, 36),
        (130, 41, 115)
    ))