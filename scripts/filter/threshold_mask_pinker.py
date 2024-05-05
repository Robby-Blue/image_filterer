
import cv2

def run_filter(r):
    image, mask = r

    m_height, m_width, _ = mask.shape
    height, width, _ = image.shape

    # TODO: use something faster
    for y in range(height):
        for x in range(width):
            pixel = image[y, x]

            mask_x = int(x*m_height/height)
            mask_y = int(y*m_width/width)
            m_pixel = mask[mask_y, mask_x]

            blueness = (pixel[0])

            if blueness > 140:
                pink = [m_pixel[0], m_pixel[1], m_pixel[2]]

                image[y, x] = pink

    return image

if __name__ == "__main__":
    cv2.imwrite("test.png", run_filter(cv2.imread("input.jpg")))