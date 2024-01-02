import sys
from os import path

from custom_exceptions import NoArgumentError, InvalidPathException

from crop_maze_image import crop_image
from image_to_grid import convert_img
from start_end_nodes_finder import find_start_end_nodes
from grid_dijkstras_algorithm import find_shortest_paths
from solution_visualizer import show_solution
from save_solution import save_solution

 
def main():
    try:
        maze_img_path = sys.argv[1:2][0]
    except IndexError:
        raise NoArgumentError from IndexError
    
    if not path.isfile(maze_img_path):
        raise InvalidPathException
   
    try:
        if sys.argv[2:3][0] == '-s':
            save = True
        else:
            save = False
    except IndexError:
        save = False

    # get save path
    try:
        save_path = sys.argv[3:4][0]
    except IndexError:
        save_path = None

    if save_path is not None and not path.isdir(save_path):
        raise InvalidPathException('\nInvalid save path.')

    maze_img = crop_image(maze_img_path) # also converts the image to black and white
    grid, scaling_factor = convert_img(maze_img)
    start_node, end_node = find_start_end_nodes(grid)
    shortest_paths = find_shortest_paths(grid, start_node)
    solution = show_solution(maze_img, scaling_factor, grid, shortest_paths, start_node, end_node)	

    if save:
        extension = maze_img_path.split('.')[-1]
        save_solution(solution, extension, save_path)


if __name__ == '__main__':
    main()

