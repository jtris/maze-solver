from typing import Tuple

import numpy as np
from custom_exceptions import InvalidMazeFormatError

'''
for identifying the second gap in case it's on the same side of the maze as the first one,

index_list: product of np.where(...), array of indexes of 0 in one of grid's sides 
returns: index of the first element that isn't consecutive (index-wise) to the previous elements
'''


def _get_index_of_nonconsecutive_occurrence(index_list):
    list_len = len(index_list)

    if list_len < 2:
        return

    for i in range(1, list_len):
        if index_list[i - 1] == index_list[i] - 1:
            continue
        return i


# completes node when given a predetermined half of it, and zeros array
def _get_single_node_value(node, zeros):
    gap_middle_index = (zeros[0] + zeros[-1]) // 2

    if node[0] == -1:
        node[0] = gap_middle_index
        return node
    node.append(gap_middle_index)
    return node


def find_start_end_nodes(grid: np.ndarray) -> tuple[tuple[int, ...], tuple[int, ...]]:
    grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1] = 1, 1, 1, 1

    top_pixels = grid[0]
    bottom_pixels = grid[-1]
    left_pixels = np.array([grid[i][0] for i in range(len(grid))])
    right_pixels = np.array([grid[i][-1] for i in range(len(grid))])
    last_row_index = len(grid) - 1
    start_node, end_node = None, None

    determined_values = {
        id(top_pixels): [0],
        id(bottom_pixels): [last_row_index],
        id(left_pixels): [-1, 0],  # -1 is just a placeholder
        id(right_pixels): [-1, last_row_index]
    }

    # find gaps (start and end node) in arrays of side pixels
    for pixels in (top_pixels, bottom_pixels, left_pixels, right_pixels):
        zeros = np.where(pixels == 0)[0]
        if len(zeros) == 0:
            continue

        nonc_index = _get_index_of_nonconsecutive_occurrence(zeros)

        # either the start or the end are on this side
        if start_node is None or end_node is None:
            if start_node is None:
                start_node = _get_single_node_value(determined_values[id(pixels)], zeros)
            else:
                end_node = _get_single_node_value(determined_values[id(pixels)], zeros)
            break

        # both the start and end are on the same side:
        start_node = determined_values[id(pixels)].copy()
        end_node = start_node.copy()

        if start_node[0] == -1:
            start_node[0] = (zeros[0] + zeros[:nonc_index][-1]) // 2
            end_node[0] = (zeros[nonc_index] + zeros[-1]) // 2
            continue

        start_node.append((zeros[0] + zeros[:nonc_index][-1]) // 2)
        end_node.append((zeros[nonc_index] + zeros[-1]) // 2)
        break

    if start_node is None:
        raise InvalidMazeFormatError('The maze image is of incorrect format, \
            it should have an entry and an exit. Neither was found.\n')

    if end_node is None:
        raise InvalidMazeFormatError('The maze image is of incorrect format, \
            it should have an entry and an exit. Only one of those was found.\n')

    return tuple(start_node), tuple(end_node)
