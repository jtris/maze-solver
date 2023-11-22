from typing import Tuple


def convert_img(image_path: str) -> Tuple:
	grid =  (
		(0, 0, 0, 0, 0, 1, 0, 0),
		(0, 0, 0, 0, 0, 1, 0, 1),
		(1, 1, 1, 0, 0, 1, 0, 1),
		(1, 1, 0, 0, 0, 1, 0, 1),
		(0, 0, 0, 0, 0, 0, 0, 0)
	)

	num_rows = len(grid)
	num_cols = len(grid[0])

	return grid, num_rows, num_cols
