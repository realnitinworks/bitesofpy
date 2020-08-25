import numpy as np
from collections import namedtuple
import re


DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1

Coordinate = namedtuple("Coordinate", "x y")


def get_grid_matrix(grid):
    """ Given a grid string, return a 2D numpy array """

    return np.array(
        [
            [
                int(j)
                for j in re.split(r' - | |\|', i)
                if j
            ]
            for i in grid.strip().splitlines()[0::2]
        ]
    )


def get_index(grid_matrix, value):
    """ Given a 2D numpy matrix and value, get the index of the
    value in the matrix as a tuple.
    """
    return np.where(grid_matrix == value)


def get_new_direction(new_coordinate, coordinate, direction):
    """
    Given the current direction
    return the new direction based on the new and old coordinates
    """
    new_direction = direction

    if new_coordinate.y - coordinate.y > 0:
        new_direction = RIGHT
    if new_coordinate.y - coordinate.y < 0:
        new_direction = LEFT
    if new_coordinate.x - coordinate.x > 0:
        new_direction = DOWN
    if new_coordinate.x - coordinate.x < 0:
        new_direction = UP

    return new_direction


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""

    grid_matrix = get_grid_matrix(grid)

    direction = RIGHT
    coordinate = Coordinate(*get_index(grid_matrix, START_VALUE))
    end_value = np.size(grid_matrix)

    print(START_VALUE, end=" ")

    for value in range(START_VALUE + 1, end_value + 1):
        new_coordinate = Coordinate(*get_index(grid_matrix, value))
        new_direction = get_new_direction(
            new_coordinate,
            coordinate,
            direction
        )

        if direction != new_direction:
            print(new_direction)
            print(value, end=" ")
            direction = new_direction
        else:
            print(value, end=" ")

        coordinate = new_coordinate
