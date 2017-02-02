__author__ = 'jalali'
import math
from enum import Enum


class PositionType(Enum):
    EMPTY = 0
    WALL = 1
    SNAKE = 2
    FOOD = 3


class GameMap:
    def __init__(self, matrix, parent, snake_head_pos, default_snake_pos,which_h):
        self.which_h =which_h
        self.parent = parent
        self.game_map = []
        self.width = len(matrix[0])
        self.height = len(matrix)
        self.head = [snake_head_pos[0], snake_head_pos[1]]
        self.snake_position = [[default_snake_pos[0][0], default_snake_pos[0][1]],
                               [default_snake_pos[1][0], default_snake_pos[1][1]],
                               [default_snake_pos[2][0], default_snake_pos[2][1]], ]
        self.food_position = []
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
        self.heuristic = 0
        self.g = 0
        self.f = self.heuristic + self.g
        self.key = str(self.snake_position[0][0]) + str(self.snake_position[0][1]) + str(
            self.snake_position[1][0]) + str(self.snake_position[1][1]) + str(self.snake_position[2][0]) + str(
            self.snake_position[2][1])

    def set_food_position(self, pos):
        self.food_position = pos
        self.game_map[pos[1]][pos[0]] = PositionType.FOOD
        if self.which_h:
            self.heuristic = self.calculate_manhattan_distance()
        else:
            self.heuristic = self.calculate_diagonal_distance()

    def calculate_manhattan_distance(self):
        # print self.food_position[0], self.food_position[1]
        # print "len snakePos=",len(self.snake_position)
        # print self.snake_position[0][0], self.snake_position[0][1]

        diff_x = math.fabs(self.head[0] - self.food_position[0])
        diff_y = math.fabs(self.head[1] - self.food_position[1])
        return diff_x + diff_y
    def calculate_diagonal_distance(self):
        diff_x = math.fabs(self.head[0] - self.food_position[0])
        diff_y = math.fabs(self.head[1] - self.food_position[1])
        return math.sqrt(math.pow(diff_y,2)+math.pow(diff_x,2))

    def get_type_of_position(self, x, y):
        return self.game_map[y][x]

    def snake_move_left(self):
        if self.head[0] == 0:
            return
        if not self.is_empty(self.head[0] - 1, self.head[1]):
            return
        self.head = [self.head[0] - 1, self.head[1]]
        self.snake_position.insert(0, self.head)
        self.game_map[self.head[1]][self.head[0]] = PositionType.SNAKE
        self.game_map[self.snake_position[-1][1]][self.snake_position[-1][0]] = PositionType.EMPTY
        # self.snake_position.remove(-1)
        del self.snake_position[-1]
        if self.which_h:
            self.heuristic = self.calculate_manhattan_distance()
        else:
            self.heuristic = self.calculate_diagonal_distance()
        self.key = str(self.snake_position[0][0]) + str(self.snake_position[0][1]) + str(
            self.snake_position[1][0]) + str(self.snake_position[1][1]) + str(self.snake_position[2][0]) + str(
            self.snake_position[2][1])

    def snake_move_right(self):
        # pass
        if self.head[0] == self.width - 1:
            return
        if not self.is_empty(self.head[0] + 1, self.head[1]):
            return
        self.head = [self.head[0] + 1, self.head[1]]
        self.snake_position.insert(0, self.head)
        self.game_map[self.head[1]][self.head[0]] = PositionType.SNAKE
        self.game_map[self.snake_position[-1][1]][self.snake_position[-1][0]] = PositionType.EMPTY
        # self.snake_position.remove()
        del self.snake_position[-1]
        if self.which_h:
            self.heuristic = self.calculate_manhattan_distance()
        else:
            self.heuristic = self.calculate_diagonal_distance()

        self.key = str(self.snake_position[0][0]) + str(self.snake_position[0][1]) + str(
            self.snake_position[1][0]) + str(self.snake_position[1][1]) + str(self.snake_position[2][0]) + str(
            self.snake_position[2][1])

    def snake_move_bottom(self):
        if self.head[1] == self.height - 1:
            return
        if not self.is_empty(self.head[0], self.head[1] + 1):
            return
        self.head = [self.head[0], self.head[1] + 1]
        # print "goooooo bottom before", self.snake_position
        self.snake_position.insert(0, self.head)
        self.game_map[self.head[1]][self.head[0]] = PositionType.SNAKE
        self.game_map[self.snake_position[-1][1]][self.snake_position[-1][0]] = PositionType.EMPTY
        del self.snake_position[-1]
        # print "goooooo bottom ", self.snake_position
        if self.which_h:
            self.heuristic = self.calculate_manhattan_distance()
        else:
            self.heuristic = self.calculate_diagonal_distance()
        self.key = str(self.snake_position[0][0]) + str(self.snake_position[0][1]) + str(
            self.snake_position[1][0]) + str(self.snake_position[1][1]) + str(self.snake_position[2][0]) + str(
            self.snake_position[2][1])

    def snake_move_top(self):
        if self.head[1] == 0:
            return
        if not self.is_empty(self.head[0], self.head[1] - 1):
            return
        self.head = [self.head[0], self.head[1] - 1]
        self.snake_position.insert(0, self.head)
        self.game_map[self.head[1]][self.head[0]] = PositionType.SNAKE
        self.game_map[self.snake_position[-1][1]][self.snake_position[-1][0]] = PositionType.EMPTY
        del self.snake_position[-1]
        if self.which_h:
            self.heuristic = self.calculate_manhattan_distance()
        else:
            self.heuristic = self.calculate_diagonal_distance()
        self.key = str(self.snake_position[0][0]) + str(self.snake_position[0][1]) + str(
            self.snake_position[1][0]) + str(self.snake_position[1][1]) + str(self.snake_position[2][0]) + str(
            self.snake_position[2][1])

    def get_map(self):
        return self.game_map

    def exist_food_in_map(self):
        for i in range(0, len(self.game_map)):
            for j in range(0, len(self.game_map[i])):
                if self.game_map[i][j] == PositionType.FOOD:
                    return True
        return False

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
            print(line)

    def get_obstacle_pos(self):
        obstacles = []
        for i in range(0, len(self.game_map)):
            for j in range(0, len(self.game_map[i])):
                if self.game_map[i][j] == PositionType.WALL:
                    obstacles.append((j, i))
        return obstacles
