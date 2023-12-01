import sys
from os import path

from custom_exceptions import NoArgumentError, InvalidPathException

from crop_maze_image import crop_image
from image_to_grid import convert_img
from start_end_nodes_finder import find_start_end_nodes
from grid_dijkstras_algorithm import find_shortest_paths


def main():
	try:
		maze_img_path = sys.argv[1:2][0]
	except IndexError:
		raise NoArgumentError from IndexError
	
	if not path.isfile(maze_img_path):
		raise InvalidPathException
	
	maze_img = crop_image(maze_img_path) # also converts the image to black and white
	grid, num_rows, num_cols = convert_img(maze_img)
	start_node, end_node = find_start_end_nodes(grid)
	shortest_paths = find_shortest_paths(grid, num_rows, num_cols, start_node)


if __name__ == '__main__':
	main()
