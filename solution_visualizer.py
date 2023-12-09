import numpy as np
import cv2


def show_solution(image: np.ndarray, scaling_factor: int, grid: np.ndarray, shortest_paths: np.ndarray,\
				  start_node: tuple[int], end_node: tuple[int]):

	NUM_ROWS = len(shortest_paths)
	NUM_COLS = len(shortest_paths[0])

	def _get_neighbours(row, col):
		neighbours = []

		if row > 0 and grid[row-1][col] != 1: # up
			neighbours.append((row-1, col))

		if row < NUM_ROWS-1 and grid[row+1][col] != 1: # down
			neighbours.append((row+1, col))

		if col > 0 and grid[row][col-1] != 1: # left
			neighbours.append((row, col-1))

		if col < NUM_COLS-1 and grid[row][col+1] != 1: # right
			neighbours.append((row, col+1))
		
		return neighbours

	
	# 1. display the solution into grid
	optimal_path = [end_node]
	current_node = end_node

	while True:
		neighbours = _get_neighbours(current_node[0], current_node[1])

		if start_node in neighbours:
			optimal_path.append(start_node)
			break

		neighbours_values = []
		for n in neighbours:
			neighbours_values.append(shortest_paths[n[0]][n[1]])

		current_node = neighbours[neighbours_values.index(min(neighbours_values))]
		optimal_path.append(current_node)

	## display

	# 2. resize

	# 3. project it onto the original cropped image


	return