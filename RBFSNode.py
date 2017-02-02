__author__ = 'jalali'
import math
from enum import Enum


class PositionType(Enum):
    EMPTY = 0
    WALL = 1
    SNAKE = 2
    FOOD = 3


class RBFSNode:
    def __init__(self, matrix, snake_pos, food_pos, parent):
        self.game_map = []
        self.head = [snake_pos[0][0], snake_pos[0][1]]
        self.height = len(matrix)
        self.width = len(matrix[0])
        for i in range(0, len(matrix)):
            temp_list = []
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == ".":
                    temp_list.append(PositionType.EMPTY)
                elif matrix[i][j] == "f":
                    # print "food.x", j
                    # print "food.y", i
                    self.food_position = [j, i]
                    temp_list.append(PositionType.FOOD)
                elif matrix[i][j] == "#":
                    temp_list.append(PositionType.WALL)
                elif matrix[i][j] == "*":
                    temp_list.append(PositionType.SNAKE)
            self.game_map.append(temp_list)
        self.food_pos = [food_pos[0], food_pos[1]]
        self.snake_pos = self.snake_pos = [[snake_pos[0][0], snake_pos[0][1]],
                                           [snake_pos[1][0], snake_pos[1][1]],
                                           [snake_pos[2][0], snake_pos[2][1]], ]
        self.parent = parent
        self.alternative_node = 99999999
        self.left_node = None
        self.right_node = None
        self.top_node = None
        self.bottom_node = None
        self.h = self.calculate_manhattan_distance()
        self.g = 0
        self.f = self.g + self.h
        self.key = str(self.snake_pos[0][0]) + str(self.snake_pos[0][1]) + str(
            self.snake_pos[1][0]) + str(self.snake_pos[1][1]) + str(self.snake_pos[2][0]) + str(
            self.snake_pos[2][1])

    def set_cost(self, cost):
        self.h = self.calculate_manhattan_distance()
        self.g = cost
        self.f = self.g + self.h

    def print_matrix(self):
        for i in range(0, len(self.game_map)):
            line = ""
            for j in range(0, len(self.game_map[i])):
                if self.game_map[i][j] == PositionType.EMPTY:
                    line += "."
                elif self.game_map[i][j] == PositionType.SNAKE:
                    line += "*"
                elif self.game_map[i][j] == PositionType.FOOD:
                    line += "f"
                elif self.game_map[i][j] == PositionType.WALL:
                    line += "#"
            print line

    def move_left(self):
        if self.head[0] == 0:
            return
        if not self.is_empty(self.head[0] - 1, self.head[1]):
            return
        self.head = [self.head[0] - 1, self.head[1]]
        self.snake_pos.insert(0, self.head)
        self.game_map[self.head[1]][self.head[0]] = PositionType.SNAKE
        self.game_map[self.snake_pos[-1][1]][self.snake_pos[-1][0]] = PositionType.EMPTY
        # self.snake_position.remove(-1)
        del self.snake_pos[-1]
        self.h = self.calculate_manhattan_distance()
        self.key = str(self.snake_pos[0][0]) + str(self.snake_pos[0][1]) + str(
            self.snake_pos[1][0]) + str(self.snake_pos[1][1]) + str(self.snake_pos[2][0]) + str(
            self.snake_pos[2][1])

    def move_right(self):
        if self.head[0] == self.width - 1:
            return
        if not self.is_empty(self.head[0] + 1, self.head[1]):
            return
        self.head = [self.head[0] + 1, self.head[1]]
        self.snake_pos.insert(0, self.head)
        self.game_map[self.head[1]][self.head[0]] = PositionType.SNAKE
        self.game_map[self.snake_pos[-1][1]][self.snake_pos[-1][0]] = PositionType.EMPTY
        # self.snake_position.remove()
        del self.snake_pos[-1]
        self.h = self.calculate_manhattan_distance()
        self.key = str(self.snake_pos[0][0]) + str(self.snake_pos[0][1]) + str(
            self.snake_pos[1][0]) + str(self.snake_pos[1][1]) + str(self.snake_pos[2][0]) + str(
            self.snake_pos[2][1])

    def move_top(self):
        if self.head[1] == 0:
            return
        if not self.is_empty(self.head[0], self.head[1] - 1):
            return
        self.head = [self.head[0], self.head[1] - 1]
        self.snake_pos.insert(0, self.head)
        self.game_map[self.head[1]][self.head[0]] = PositionType.SNAKE
        self.game_map[self.snake_pos[-1][1]][self.snake_pos[-1][0]] = PositionType.EMPTY
        del self.snake_pos[-1]
        self.h = self.calculate_manhattan_distance()
        self.key = str(self.snake_pos[0][0]) + str(self.snake_pos[0][1]) + str(
            self.snake_pos[1][0]) + str(self.snake_pos[1][1]) + str(self.snake_pos[2][0]) + str(
            self.snake_pos[2][1])

    def move_bottom(self):
        if self.head[1] == self.height - 1:
            return

        if not self.is_empty(self.head[0], self.head[1] + 1):
            return
        self.head = [self.head[0], self.head[1] + 1]
        # print "goooooo bottom before", self.snake_position
        self.snake_pos.insert(0, self.head)
        self.game_map[self.head[1]][self.head[0]] = PositionType.SNAKE
        self.game_map[self.snake_pos[-1][1]][self.snake_pos[-1][0]] = PositionType.EMPTY
        del self.snake_pos[-1]
        # print "goooooo bottom ", self.snake_position
        self.h = self.calculate_manhattan_distance()
        self.key = str(self.snake_pos[0][0]) + str(self.snake_pos[0][1]) + str(
            self.snake_pos[1][0]) + str(self.snake_pos[1][1]) + str(self.snake_pos[2][0]) + str(
            self.snake_pos[2][1])

    def calculate_manhattan_distance(self):
        diff_x = math.fabs(self.head[0] - self.food_pos[0])
        diff_y = math.fabs(self.head[1] - self.food_pos[1])
        return diff_x + diff_y

    def is_wall(self, x, y):
        if self.game_map[y][x] == PositionType.WALL:
            return True
        return False

    def is_food(self, x, y):
        if self.game_map[y][x] == PositionType.FOOD:
            return True
        return False

    def is_empty(self, x, y):
        if self.game_map[y][x] == PositionType.EMPTY or self.game_map[y][x] == PositionType.FOOD:
            return True
        return False

    def is_snake(self, x, y):
        if self.game_map[y][x] == PositionType.SNAKE:
            return True
        return False

    def get_obstacle_pos(self):
        obstacles = []
        for i in range(0, len(self.game_map)):
            for j in range(0, len(self.game_map[i])):
                if self.game_map[i][j] == PositionType.WALL:
                    obstacles.append((j, i))
        return obstacles

    def get_matrix(self):
        my_map = []
        for i in range(0, len(self.game_map)):
            temp_map = []
            for j in range(0, len(self.game_map[i])):
                if self.game_map[i][j] == PositionType.EMPTY:
                    temp_map.append(".")
                elif self.game_map[i][j] == PositionType.SNAKE:
                    temp_map.append("*")
                elif self.game_map[i][j] == PositionType.FOOD:
                    temp_map.append("f")
                elif self.game_map[i][j] == PositionType.WALL:
                    temp_map.append("#")
            my_map.append(temp_map)
        return my_map
