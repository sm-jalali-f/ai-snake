__author__ = 'jalali'
from enum import Enum


class PositionType(Enum):
    EMPTY = 0
    WALL = 1
    SNAKE = 2
    FOOD = 3


def get_map(matrix):
    game_map = []
    for i in matrix:
        temp = []
        for j in matrix:
            temp.append(PositionType.EMPTY)
        game_map.append(temp)
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == ".":
                game_map[col][row] == PositionType.EMPTY
            if matrix[row][col] == "#":
                game_map[col][row] == PositionType.WALL
            if matrix[row][col] == "f":
                game_map[col][row] == PositionType.FOOD
            if matrix[row][col] == "*":
                game_map[col][row] == PositionType.SNAKE
    return game_map
