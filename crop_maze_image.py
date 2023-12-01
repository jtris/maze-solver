import numpy as np
import cv2


def crop_image(path: str) -> np.ndarray:
    img = cv2.imread(path)
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # convert to black and white
    (_, black_white_img) = cv2.threshold(grey_img, 127, 255, cv2.THRESH_BINARY)

    # crop image
    zeros_occurences = np.where(black_white_img == 0)[0]
    top_line_index = zeros_occurences[0]
    bottom_line_index = zeros_occurences[-1] + 1

    zeros_occurences = np.where(black_white_img[top_line_index] == 0)[0]
    l_line_index = zeros_occurences[0]
    r_line_index = zeros_occurences[-1] + 1

    black_white_img = black_white_img[top_line_index:bottom_line_index, l_line_index:r_line_index]

    return black_white_img