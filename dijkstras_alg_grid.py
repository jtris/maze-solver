'''
input: 
		(1)  a grid where a 0 is a free space and a 1 is a wall
			 for example:
			
					0 0 0 0 0 1 0 0
					0 0 0 0 0 1 0 1
					1 1 1 0 0 1 0 1
					1 1 0 0 0 1 0 1
					0 0 0 0 0 0 0 0

		(2) a starting point as a tuple (row, col)

		(3) an ending point as a tuple (row, col)


output: a list of nodes along the path  [(x0, y0), (x1, y1), ..., (xn, yn)]
'''

import sys


GRID =  [
	[0, 0, 0, 0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0, 1, 0, 1],
	[1, 1, 1, 0, 0, 1, 0, 1],
	[1, 1, 0, 0, 0, 1, 0, 1],
	[0, 0, 0, 0, 0, 0, 0, 0]
]

NUM_ROWS = 5
NUM_COLS = 8
MAX_VALUE = sys.maxsize

START_NODE = (NUM_ROWS-1, 0)
END_NODE = (0, NUM_COLS-1)


def get_node_neighbours(node):
	neighbours = []
	
	if node[0] > 0 and GRID[node[0]-1][node[1]] != 1: # down
		neighbours.append((node[0]-1, node[1]))

	if node[0] < NUM_ROWS-1 and GRID[node[0]+1][node[1]] != 1: # up
		neighbours.append((node[0]+1, node[1]))

	if node[1] > 0 and GRID[node[0]][node[1]-1] != 1: # left
		neighbours.append((node[0], node[1]-1))

	if node[1] < NUM_COLS-1 and GRID[node[0]][node[1]+1] != 1: # right
		neighbours.append((node[0], node[1]+1)) 
	
	return neighbours


def solve():

	# stores coordinates of each unvisited node
	unvisited_nodes = [(row, col) for row in range(NUM_ROWS) for col in range(NUM_COLS)] 		# [(r, c), (r, c), ...]

	shortest_path_costs = [[MAX_VALUE for col in range(NUM_COLS)] for row in range(NUM_ROWS)] # [[mv, mv, ...], [mv, mv, ...]]
	shortest_path_costs[START_NODE[0]][START_NODE[1]] = 0
	

	while unvisited_nodes:
		current_min_node = None
			
		# find the node with the lowest value
		for node in unvisited_nodes:
			if current_min_node == None:
				current_min_node = node			
			elif shortest_path_costs[node[0]][node[1]] < shortest_path_costs[current_min_node[0]][current_min_node[1]]:
				current_min_node = node

		# visit all unvisited neighbours, adjust shortest_path_costs[]
		neighbours = get_node_neighbours(current_min_node)

		for neighbour in neighbours:
			tentative_value = shortest_path_costs[current_min_node[0]][current_min_node[1]] + 1

			# update neighbour values
			if tentative_value < shortest_path_costs[neighbour[0]][neighbour[1]]:
				shortest_path_costs[neighbour[0]][neighbour[1]] = tentative_value
		
		unvisited_nodes.pop(unvisited_nodes.index((current_min_node[0], current_min_node[1])))

	return shortest_path_costs


def print_result(shortest_path_costs):
	if shortest_path_costs[END_NODE[0]][END_NODE[1]] == MAX_VALUE:
		print('Impossible requirements.\n')
		return None

	optimal_path = [END_NODE]
	current_node = END_NODE

	while(True):
		neighbours = get_node_neighbours(current_node)
		
		if START_NODE in neighbours:
			optimal_path.append(START_NODE)
			break
		
		neighbours_values = []
		for neighbour in neighbours:
			neighbours_values.append(shortest_path_costs[neighbour[0]][neighbour[1]])

		current_node = neighbours[neighbours_values.index(min(neighbours_values))]
		optimal_path.append(current_node)

	print(optimal_path)


def main():
	shortest_path_costs = solve()
	print_result(shortest_path_costs)


if __name__ == '__main__':
	main()