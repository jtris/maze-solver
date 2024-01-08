import numpy as np
import cv2

from custom_exceptions import InvalidImageFormatError, InvalidMazeFormatError


def crop_image(path: str) -> np.ndarray:
    img = cv2.imread(path)

    try:
        grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        raise InvalidImageFormatError

    # convert to black and white
    (_, black_white_img) = cv2.threshold(grey_img, 127, 255, cv2.THRESH_BINARY)

    zeros_occurences = np.where(black_white_img == 0)[0]
    
    if len(zeros_occurences) == 0:
        raise InvalidMazeFormatError(message="Incorrect maze format. Wasn't alble to find any walls.")
    
    top_line_index = zeros_occurences[0]
    bottom_line_index = zeros_occurences[-1] + 1

    zeros_occurences = np.where(black_white_img[top_line_index] == 0)[0]
    l_line_index = zeros_occurences[0]
    r_line_index = zeros_occurences[-1] + 1

    cropped_black_white_img = black_white_img[top_line_index:bottom_line_index, l_line_index:r_line_index]

    return cropped_black_white_img
