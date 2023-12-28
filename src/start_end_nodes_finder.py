from numpy import ndarray, array
from custom_exceptions import InvalidMazeFormatError


def find_start_end_nodes(grid: ndarray) -> tuple[int]:
	
	top_pixels = grid[0]
	bottom_pixels = grid[-1]
	left_pixels = array([grid[i][0] for i in range(len(grid))])
	right_pixels = array([grid[i][-1] for i in range(len(grid))])
	last_row_index = len(grid)-1

	values = {
		id(top_pixels) : [0],
		id(bottom_pixels) : [last_row_index],
		id(left_pixels) : [-1, 0], # -1 is just a placeholder
		id(right_pixels) : [-1, last_row_index]
	}

	start_node = []
	end_node = []

	first_gap_occured = False
	second_gap_occured = False
	start_node_first_index = -1
	start_node_last_index = -1
	end_node_first_index = -1
	end_node_last_index = -1
	first_done = False
	second_done = False
	
	for pixels in (top_pixels, bottom_pixels, left_pixels, right_pixels):
		pixels[0], pixels[-1] = 1, 1
		
		if second_gap_occured:
			break

		for i in range(len(pixels)):
			if pixels[i] == 0:
				if not first_gap_occured:
					first_gap_occured = True
					start_node_first_index = i

				# elif start_node_last_index != -1 and not second_gap_occured and not (i == start_node_first_index+1 and first_done == False):
				elif start_node_last_index != -1 and not second_gap_occured and i != start_node_first_index+1:
					second_gap_occured = True
					end_node_first_index = i
				else: continue
			else:
				if pixels[i-1] == 0:
					if start_node_last_index == -1:
						start_node_last_index = i-1
					elif end_node_first_index != -1 and end_node_last_index == -1:
						end_node_last_index = i-1

		# when we finish iterating over pixels of a side, but we didn't encounter an end to a gap:
		if not first_done and first_gap_occured:
			if start_node_last_index == -1:
				start_node_last_index = len(pixels)-1
			
			start_node = values[id(pixels)].copy()
			first_done = True

			if len(start_node) == 1:
				start_node.append((start_node_first_index+start_node_last_index)//2)
			else: # it's either [-1, 0] or [-1, last_row_index]
				start_node[0] = (start_node_first_index+start_node_last_index)//2
		
		if not second_done and second_gap_occured:
			if end_node_last_index == -1:
				end_node_last_index = len(pixels)-1
			
			end_node = values[id(pixels)]
			second_done = True

			if len(end_node) == 1:
				end_node.append((end_node_first_index+end_node_last_index)//2)
			else:
				end_node[0] = (end_node_first_index+end_node_last_index)//2

	if not second_gap_occured:
		raise InvalidMazeFormatError('The maze image is of incorrect format, \
			it should have an entry and an exit. Only one of those was found.\n')

	if not first_gap_occured:
		raise InvalidMazeFormatError('The maze image is of incorrect format, \
			it should have an entry and an exit. Neither was found.\n')

	return tuple(start_node), tuple(end_node)
