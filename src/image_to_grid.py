import cv2
import numpy as np


def convert_img(image: np.ndarray) -> np.ndarray | tuple | int:
    num_rows_img = len(image)
    num_cols_img = len(image[0])
    total_px_count = num_rows_img * num_cols_img

    # scaling factor thresholds
    SF_1_THRESH = 10_000  # ~ 100x100
    SF_2_THRESH = 40_000  # ~ 200x200
    SF_3_THRESH = 100_000 # ~ 330x330 
    SF_4_THRESH = 160_000 # ~ 400x400

    if total_px_count < SF_1_THRESH:
        scaling_factor = 1
    elif total_px_count < SF_2_THRESH:
        scaling_factor = 2
    elif total_px_count < SF_3_THRESH:
        scaling_factor = 3
    elif total_px_count < SF_4_THRESH:
        scaling_factor = 4
    else:
        scaling_factor = 5

    resized_image = cv2.resize(image, (num_rows_img//scaling_factor, num_cols_img//scaling_factor))

    num_rows_resized, num_cols_resized = resized_image.shape
    grid = []
    for r in range(num_rows_resized):
        grid.append([])
        for c in range(num_cols_resized):
            grid[r].append(0 if resized_image[r][c] == 255 else 1)

    grid = np.asarray(grid)

    return grid, scaling_factor
