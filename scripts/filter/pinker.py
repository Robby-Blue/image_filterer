def run_filter(image):
    height, width, _ = image.shape

    # TODO: use something faster
    for y in range(height):
        for x in range(width):
            pixel = image[y, x]

            blueness = (255-pixel[0])
            
            pink = [255-blueness, 0, 255-blueness]

            image[y, x] = pink

    return image