from os import chdir
from cv2 import imwrite
from numpy import ndarray


def save_solution(image: ndarray, extension: str, save_path: str):
    if save_path is not None:
        chdir(save_path)

    imwrite('solution.'+extension, image)

