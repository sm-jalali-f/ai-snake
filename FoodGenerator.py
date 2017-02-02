__author__ = 'jalali'
import random
from GameMap import PositionType

class FoodGenerator:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.game_map =[]
        self.width = 0
        self.height = 0

    def generate_food(self, game_map):
        self.game_map = game_map
        self.height = len(self.game_map)
        random.random()

        if self.height > 0:
            self.width = len(self.game_map[0])

        x = 0
        y = 0
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.is_possible_food(self.game_map, x, y):
                break
        self.x = x
        self.y = y

        return [x, y]

    def is_possible_food(self, game_map, x, y):
        if game_map[y][x] == PositionType.WALL or game_map[y][x] == PositionType.SNAKE:
            return False
        count = 0
        if y != 0:
            if game_map[y - 1][x] == PositionType.EMPTY:  # check above
                count += 1
        if y != self.height-1:
            if game_map[y+1][x] == PositionType.EMPTY:  # check below
                count += 1
        if x != 0:
            if game_map[y][x-1] == PositionType.EMPTY:  # check left
                count += 1
        if x != self.width-1:
            if game_map[y][x+1] == PositionType.EMPTY:  # check right
                count += 1
        if count < 2:
            return False
        # TODO check exist a path from ai-snake to food
        return True
