import cv2
import sys
import numpy as np
from os import path

from custom_exceptions import NoArgumentError, InvalidPathException


def main():
    try:
        maze_img_path = sys.argv[1:2][0]
        
    except IndexError:
        raise NoArgumentError from IndexError
    
    try:
        iterations = int(sys.argv[2:3][0])
    except:
        iterations = 1

    if not path.isfile(maze_img_path):
        raise InvalidPathException 

    img = cv2.imread(maze_img_path)
    extension = maze_img_path.split('.')[-1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilate = cv2.erode(img, kernel, iterations=iterations)
    cv2.imwrite('maze_dilated.' + extension, dilate)


if __name__ == '__main__':
    main()

