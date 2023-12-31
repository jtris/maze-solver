import numpy as np
import cv2


def show_solution(image: np.ndarray, scaling_factor: int, grid: np.ndarray, shortest_paths: np.ndarray,\
                  start_node: tuple[int], end_node: tuple[int]):

    original_num_rows, original_num_cols = image.shape
    NUM_ROWS, NUM_COLS = shortest_paths.shape
    BLUE = (255, 0, 0)
    BLACK = (0, 0, 0)


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
    

    # display the solution into grid
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

    # only draw the path onto a black image, resizing would damage the quality of the original
    path_image = np.full((NUM_ROWS, NUM_COLS, 3), BLACK, dtype=np.uint8)

    for (r, c) in optimal_path:
        path_image[r][c] = BLUE

    path_image = cv2.resize(path_image, (original_num_cols, original_num_rows))

    # thicken the path line
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    path_image = cv2.dilate(path_image, kernel, iterations=2)

    # convert back to bgr to draw the path
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    # project it onto the original cropped image
    for row in range(original_num_rows):
        for col in range(original_num_cols):
            if path_image[row, col, 0] > 150:
                image[row, col] = BLUE

    cv2.imshow('', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

