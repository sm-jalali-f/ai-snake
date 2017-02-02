__author__ = 'jalali'
from ReadFile import ReadFile
import sys
from AStarSearch import AStarSearch
from GameMap import GameMap
import pygame
from pygame.locals import *
from time import sleep
from FoodGenerator import FoodGenerator
from RBFSearch import *
from RBFSNode import *
from SnakeMap import *

MAX_REWARD = 30
# print sys.argv


def draw_table(map_len, map_length):
    black = (0, 0, 0)
    screen_color = (229, 189, 2)
    screen = pygame.display.set_mode((map_length, map_length))
    screen.fill(screen_color)

    # outers lines
    pygame.display.update()
    pygame.draw.lines(screen, black, True, [(0, 0), (map_length, 0)], 7)
    pygame.draw.lines(screen, black, True, [(0, 0), (0, map_length)], 7)
    pygame.draw.lines(screen, black, True, [(0, map_length), (map_length, map_length)], 7)
    pygame.draw.lines(screen, black, True, [(map_length, 0), (map_length, map_length)], 7)
    pygame.display.update()

    i = 0
    while i <= map_length:  # vertical lines
        pygame.draw.lines(screen, black, True, [(i, 0), (i, map_length)], 2)
        i += map_length / map_len
    i = 0
    while i <= map_length:  # horizontal lines
        pygame.draw.lines(screen, black, True, [(0, i), (map_length, i)], 2)
        i += map_length / map_len  # 30
    pygame.display.update()
    return screen


def draw_obstacles(map_len, screen, obstacles, map_length):
    obstacle_color = (229, 44, 2)
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color,
                         (obstacle[1] * map_length / map_len + 1, obstacle[0] * map_length / map_len + 1,
                          map_length / map_len, map_length / map_len), 0)
    pygame.display.update()


def draw_snake(map_len, screen, snake, map_length):
    snake_color = (0, 0, 0)
    for pos in snake:
        pygame.draw.rect(screen, snake_color, (pos[1] * map_length / map_len + 1, pos[0] * map_length / map_len + 1,
                                               map_length / map_len, map_length / map_len), 0)
    pygame.display.update()


def draw_food(map_len, screen, food_pos, map_length):
    food_color = (0, 166, 244)
    pygame.draw.rect(screen, food_color,
                     (food_pos[1] * map_length / map_len + 1, food_pos[0] * map_length / map_len + 1,
                      map_length / map_len, map_length / map_len))


if len(sys.argv) > 0:
    # x = ReadFile(sys.argv[1], "map-out.txt")
    x = ReadFile("test.txt", "map-out.txt")
    t = x.read_file()

    food_fen = FoodGenerator()

    for m in range(0,11):
        init_state = GameMap(t, None, [0, 2], [[0, 2], [0, 1], [0, 0]], True)
        init_state_diagonal = GameMap(t, None, [0, 2], [[0, 2], [0, 1], [0, 0]], False)
        init_state.set_food_position(food_fen.generate_food(init_state.game_map))
        init_state_diagonal.set_food_position(food_fen.generate_food(init_state.game_map))

        movement_list_manhattan = []
        movement_list_diagonal = []
        for i in range(0, 30):
            # print "Score=", i
            mySearch = AStarSearch(init_state)
            diagonalSearch = AStarSearch(init_state_diagonal)
            diagonalSearch.start_search(False)
            mySearch.start_search(True)
            answer = mySearch.get_answer()
            answer_diagonal = diagonalSearch.get_answer()
            movement_list_manhattan.append(len(answer) - 1)
            movement_list_diagonal.append(len(answer_diagonal) - 1)
            pygame.init()
            map_length = 300
            screen = draw_table(len(t), map_length)
            draw_obstacles(len(t), screen, answer[0].get_obstacle_pos(), map_length)
            draw_snake(len(t), screen, answer[0].snake_position, map_length)
            draw_food(len(t), screen, answer[0].food_position, map_length)

            index = 0
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()
                sleep(0.08)
                if index < len(answer):
                    screen = draw_table(len(t), map_length)
                    draw_obstacles(len(t), screen, answer[0].get_obstacle_pos(), map_length)
                    draw_snake(len(t), screen, answer[index].snake_position, map_length)
                    draw_food(len(t), screen, answer[0].food_position, map_length)
                else:
                    break
                index += 1
            init_state = GameMap(answer[-1].get_matrix(), None, answer[-1].snake_position[0], answer[-1].snake_position,
                                 True)
            init_state_diagonal = GameMap(answer_diagonal[-1].get_matrix(), None, answer_diagonal[-1].snake_position[0],
                                 answer_diagonal[-1].snake_position, False)
            init_state.set_food_position(food_fen.generate_food(init_state.game_map))
            init_state_diagonal.set_food_position(food_fen.generate_food(init_state_diagonal.game_map))
            # init_state.
        print ("id =",m," -->  manhattan avg move=", sum(movement_list_manhattan) / len(movement_list_manhattan))
        print ("id =",m," -->  diagonal avg move=", sum(movement_list_diagonal) / len(movement_list_diagonal))
