__author__ = 'jalali'
import math
from RBFSNode import RBFSNode
# from enum import Enum
from SnakeMap import *
from time import sleep


# class PositionType(Enum):
#     EMPTY = 0
#     WALL = 1
#     SNAKE = 2
#     FOOD = 3


class RbfsSearch:
    def __init__(self):
        self.open_list = []
        self.answer_list = []

    def print_answer(self, last_node):
        node = last_node
        obstacle = []
        for i in range(0, node.width):
            for j in range(0, node.width):
                if node.game_map[i][j] == PositionType.WALL:
                    obstacle.append((j, i))
        # selfanswer_list= []
        while node is not None:
            self.answer_list.append(node)
            node = node.parent
        self.answer_list.reverse()

    def exist_in_open_list(self, state):
        # print " exist in close list"
        for i in range(0, len(self.open_list)):
            if self.open_list[i].key == state.key:
                return True
        return False

    def insert_to_open_list(self, state):
        index = 0
        for item in self.open_list:
            if item.f < state.f:
                index += 1
            else:
                break
        self.open_list.insert(index, state)

    def remove_from_open_list(self, state):
        index = 0
        for item in self.open_list:
            if item.key == state.key:
                del self.open_list[index]
                return
            index += 1

    def start_search(self, init_state, f_limit):
        while True:
            if init_state.h == 0:
                return init_state
            bottom_node = RBFSNode(init_state.get_matrix(), init_state.snake_pos, init_state.food_pos, init_state)
            bottom_node.move_bottom()
            top_node = RBFSNode(init_state.get_matrix(), init_state.snake_pos, init_state.food_pos, init_state)
            top_node.move_top()
            left_node = RBFSNode(init_state.get_matrix(), init_state.snake_pos, init_state.food_pos, init_state)
            left_node.move_left()
            right_node = RBFSNode(init_state.get_matrix(), init_state.snake_pos, init_state.food_pos, init_state)
            right_node.move_right()
            successors = []
            if bottom_node.key != init_state.key:
                bottom_node.g = init_state.g + 1
                successors.append(bottom_node)
            if top_node.key != init_state.key:
                top_node.g = init_state.g + 1
                successors.append(top_node)
            if left_node.key != init_state.key:
                left_node.g = init_state.g + 1
                successors.append(left_node)
            if right_node.key != init_state.key:
                right_node.g = init_state.g + 1
                successors.append(right_node)
            if len(successors) == 0:
                return None, 9999999
            for s in successors:
                s.f = max(s.g + s.h, s.f)

            while True:
                successors.sort(lambda x, y: int(x.f) - int(y.f))  # Order by lowest f value
                best = successors[0]
                if best.f > f_limit:
                    init_state.f = best.f
                if len(successors)> 1:
                    alternative = successors[1]
                else:
                    alternative = best.parent
                result, best.f = self.start_search(best, min(f_limit, alternative))
                if result is not None:
                    return result
