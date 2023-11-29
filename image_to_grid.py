import cv2
import numpy as np


def convert_img(image: np.ndarray) -> tuple | int:
	total_px_count = len(image)*len(image[0])

	if total_px_count < 13_000:
		scaling_factor = 1
	elif total_px_count < 52_000:
		scaling_factor = 2
	elif total_px_count < 117_000:
		scaling_factor = 3
	else:
		scaling_factor = 4

	image = cv2.resize(image, (len(image)//scaling_factor, len(image[0])//scaling_factor))

	grid = []

	num_rows_img = len(image)
	num_cols_img = len(image[0])

	for r in range(num_rows_img):
		grid.append([])
		for c in range(num_cols_img):
			grid[r].append(0 if image[r][c] == 255 else 1)

	grid = np.asarray(grid)

	num_rows = len(grid)
	num_cols = len(grid[0])

	return grid, num_rows, num_cols
