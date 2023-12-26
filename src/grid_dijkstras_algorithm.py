import sys
from numpy import ndarray, asarray


def _get_node_neighbours(node, grid, num_rows, num_cols):
	neighbours = []
	
	if node[0] > 0 and grid[node[0]-1][node[1]] != 1: # up
		neighbours.append((node[0]-1, node[1]))

	if node[0] < num_rows-1 and grid[node[0]+1][node[1]] != 1: # down
		neighbours.append((node[0]+1, node[1]))

	if node[1] > 0 and grid[node[0]][node[1]-1] != 1: # left
		neighbours.append((node[0], node[1]-1))

	if node[1] < num_cols-1 and grid[node[0]][node[1]+1] != 1: # right
		neighbours.append((node[0], node[1]+1)) 
	
	return neighbours


# the grid parameter is a 2D numpy array with 0's representing empty spaces and 1's representing walls
# returns the same grid, but with the corresponding path length in place of each node

def find_shortest_paths(grid: ndarray, start_node: tuple[int]) -> ndarray:
	num_rows, num_cols = grid.shape

	# stores coordinates of each unvisited node: [(r, c), (r, c), ...]
	unvisited_nodes = [(row, col) for row in range(num_rows) for col in range(num_cols)]

	# same shape as grid
	shortest_path_costs = [[sys.maxsize for col in range(num_cols)] for row in range(num_rows)]
	shortest_path_costs[start_node[0]][start_node[1]] = 0
	
	while unvisited_nodes:
		current_min_node = None
			
		# find the node with the lowest value
		for node in unvisited_nodes:
			if current_min_node == None:
				current_min_node = node
			elif shortest_path_costs[node[0]][node[1]] < shortest_path_costs[current_min_node[0]][current_min_node[1]]:
				current_min_node = node

		neighbours = _get_node_neighbours(current_min_node, grid, num_rows, num_cols)

		for neighbour in neighbours:
			tentative_value = shortest_path_costs[current_min_node[0]][current_min_node[1]] + 1

			# update neighbour values
			if tentative_value < shortest_path_costs[neighbour[0]][neighbour[1]]:
				shortest_path_costs[neighbour[0]][neighbour[1]] = tentative_value
		
		unvisited_nodes.pop(unvisited_nodes.index((current_min_node[0], current_min_node[1])))

	return asarray(shortest_path_costs)
