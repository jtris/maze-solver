"""
todo:
convert all the uncessary lists to tuples 
"""


import sys
from os import path

from image_to_grid import convert_img
from grid_start_node_finder import find_start_node
from grid_dijkstras_algorithm import find_shortest_paths


class InvalidPathException(Exception):
	def __init__(self, message='\n\nIncorrect Path, Please enter a valid path to an image of a maze.'):
		self.message = message
		super().__init__(self.message)


def main():
	maze_img_path = sys.argv[1:2][0]

	if not path.isfile(maze_img_path):
		raise InvalidPathException

	grid, num_rows, num_cols = convert_img(maze_img_path)
	start_node = find_start_node(grid)
	shortest_paths = find_shortest_paths(grid, num_rows, num_cols, start_node)


if __name__ == '__main__':
	main()
