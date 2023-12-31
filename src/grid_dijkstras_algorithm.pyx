import sys
import Cython
from numpy import asarray


cdef list _get_node_neighbours(node, int[:, :] grid, int num_rows, int num_cols):
    cdef list neighbours = []

    if node[0] > 0 and grid[node[0]-1][node[1]] != 1: # up
        neighbours.append((node[0]-1, node[1]))

    if node[0] < num_rows-1 and grid[node[0]+1][node[1]] != 1: # down
        neighbours.append((node[0]+1, node[1]))

    if node[1] > 0 and grid[node[0]][node[1]-1] != 1: # left
        neighbours.append((node[0], node[1]-1))

    if node[1] < num_cols-1 and grid[node[0]][node[1]+1] != 1: # right
        neighbours.append((node[0], node[1]+1)) 
    
    return neighbours


cpdef find_shortest_paths(int[:, :] grid, tuple start_node):
    cdef unsigned int num_rows = len(grid)
    cdef unsigned int num_cols = len(grid[0]) 
    cdef list neighbours
    cdef unsigned long long tentative_value
    cdef tuple current_min_node

    # stores coordinates of each unvisited node: [(r, c), (r, c), ...]
    cdef list[num_rows][num_cols] unvisited_nodes = [(row, col) for row in range(num_rows) for col in range(num_cols)]

    # same shape as grid
    cdef list[num_rows][num_cols] shortest_path_costs = [[sys.maxsize for col in range(num_cols)] for row in range(num_rows)]
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
