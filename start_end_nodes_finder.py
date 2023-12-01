import numpy as np
from custom_exceptions import InvalidMazeFormatException


def find_start_end_nodes(grid: np.ndarray) -> tuple[int, int]:

	top_pixels = grid[0]
	bottom_pixels = grid[-1]
	left_pixels = np.array([grid[i][0] for i in range(len(grid))])
	right_pixels = np.array([grid[i][-1] for i in range(len(grid))])

	start_node = []
	end_node = []

	if 0 in top_pixels:
		zeros = np.where(top_pixels == 0)[0]
		fist_0 = zeros[0]
		last_0 = zeros[-1]

		start_node.append(0)
		start_node.append((last_0 - fist_0) // 2 + fist_0)

	if 0 in bottom_pixels:
		zeros = np.where(bottom_pixels == 0)[0]
		fist_0 = zeros[0]
		last_0 = zeros[-1]
		
		for node in (start_node, end_node):
			if len(node) >= 2:
				continue
			
			node.append(len(grid)-1)
			node.append((last_0 - fist_0) // 2 + fist_0)
			break

	if 0 in left_pixels:
		zeros = np.where(left_pixels == 0)[0]
		fist_0 = zeros[0]
		last_0 = zeros[-1]
		
		for node in (start_node, end_node):
			if len(node) >= 2:
				continue
	
			node.append((last_0 - fist_0) // 2 + fist_0)
			node.append(0)
			break

	if 0 in right_pixels:
		zeros = np.where(right_pixels == 0)[0]
		fist_0 = zeros[0]
		last_0 = zeros[-1]
		
		for node in (start_node, end_node):
			if len(node) >= 2:
				continue

			node.append((last_0 - fist_0) // 2 + fist_0)
			node.append(len(grid)-1)
			break

	if not len(start_node) == 2 and len(end_node) == 2:
		raise InvalidMazeFormatException('The maze image is of incorrect format, \
										it should have an entry and an exit.\n')

	return start_node, end_node
