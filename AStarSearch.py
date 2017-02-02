__author__ = 'jalali'
from GameMap import GameMap, PositionType
from time import sleep
from graphics import draw_map
from graphics import *


class AStarSearch:
    def __init__(self, initial_state):
        self.open_list = []
        self.close_list = []
        self.init_state = initial_state
        self.answer_list = []
        pass

    def start_search(self,which_h):
        self.open_list.append(self.init_state)
        main_node = None
        while len(self.open_list) > 0:
            # print "openList Size =", len(self.open_list)
            main_node = self.open_list.pop(0)
            # print "pop node :"
            # main_node.print_matrix()
            # print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
            self.close_list.append(main_node)
            if main_node.heuristic == 0:
                # print "exist answer"
                self.print_answer(main_node)
                break
            # print "================================================"
            # print "bottom:"
            bottom_node = GameMap(main_node.get_matrix(), main_node, main_node.head, main_node.snake_position,which_h)
            bottom_node.snake_move_bottom()
            # bottom_node.print_matrix()
            if not self.exist_in_close(bottom_node):
                bottom_node.g = main_node.g + 1
                bottom_node.f = max(bottom_node.f, bottom_node.g + bottom_node.heuristic)
                # print "f=", bottom_node.f
                self.update_open_list(bottom_node)
            # print "================================================"
            # print "left:"
            # print "snake_pos main", main_node.snake_position
            left_node = GameMap(main_node.get_matrix(), main_node, main_node.head, main_node.snake_position,which_h)
            left_node.snake_move_left()
            # left_node.print_matrix()
            if not self.exist_in_close(left_node):
                left_node.g = main_node.g + 1
                left_node.f = max(left_node.f, left_node.g + left_node.heuristic)
                # print "f=", left_node.f
                self.update_open_list(left_node)
            # print "================================================"
            # print "right:"
            right_node = GameMap(main_node.get_matrix(), main_node, main_node.head, main_node.snake_position,which_h)
            right_node.snake_move_right()
            # right_node.print_matrix()
            if not self.exist_in_close(right_node):
                right_node.g = main_node.g + 1
                right_node.f = max(right_node.f, right_node.g + right_node.heuristic)
                # print "f=", right_node.f
                self.update_open_list(right_node)
            # print "================================================"
            # print "top:"
            top_node = GameMap(main_node.get_matrix(), main_node, main_node.head, main_node.snake_position,which_h)
            top_node.snake_move_top()
            # top_node.print_matrix()
            if not self.exist_in_close(top_node):
                top_node.g = main_node.g + 1
                top_node.f = max(top_node.f, top_node.g + top_node.heuristic)
                # print "f=", top_node.f
                self.update_open_list(top_node)

                # self.print_answer(main_node)

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

        # for i in range(0, len(self.answer_list)):
        #     snake_tuple_pos = []
        #     tuple1 = (self.answer_list[i].snake_position[0][0], self.answer_list[i].snake_position[0][1])
        #     snake_tuple_pos.append(tuple1)
        #     tuple1 = (self.answer_list[i].snake_position[1][0], self.answer_list[i].snake_position[1][1])
        #     snake_tuple_pos.append(tuple1)
        #     tuple1 = (self.answer_list[i].snake_position[2][0], self.answer_list[i].snake_position[2][1])
        #     snake_tuple_pos.append(tuple1)
        #     # if i== 0:
        #     draw_map(self.answer_list[i].width, obstacle, snake_tuple_pos,
        #              (self.answer_list[i].food_position[0], self.answer_list[i].food_position[1]))
        #     # else:
        #     sleep(0.5)
        #     # print node.snake_position[0][0], node.snake_position[0][1]

    def exist_in_close(self, state):
        # print " exist in close list"
        for i in range(0, len(self.close_list)):
            # print "state.key ", state.key
            # print "closeList[", i, "].key ", self.close_list[i].key
            if self.close_list[i].key == state.key:
                return True
        return False

    def update_open_list(self, state):
        # print "Update open list:"
        index = 0
        for i in range(0, len(self.open_list)):
            if self.open_list[i].f < state.f:
                index += 1
            # print "state.key ", state.key
            # print "openlist[",i,"].key ", self.open_list[i].key
            if state.key == self.open_list[i].key:
                if self.open_list[i].g > state.g:
                    self.open_list.g = state.g
                    self.open_list.parent = state.parent
                    return
        self.open_list.insert(index, state)

    def get_answer(self):
        return self.answer_list
