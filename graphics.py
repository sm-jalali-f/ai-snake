__author__ = 'jalali'
import pygame, sys
from pygame.locals import *

pygame.init()


def draw_map(map_len, obstacles_pos, snake_pos, food_pos):
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
            pygame.draw.rect(screen, obstacle_color, (obstacle[1] * map_length / map_len + 1, obstacle[0] * map_length / map_len + 1,
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
        pygame.draw.rect(screen, food_color, (food_pos[1] * map_length / map_len + 1, food_pos[0] * map_length / map_len + 1,
                                              map_length / map_len, map_length / map_len))
    #  this is the code you need to customize
    map_length = map_len
    screen = draw_table(map_len, map_length)
    draw_obstacles(map_len, screen, obstacles_pos, map_length)
    draw_snake(map_len, screen, snake_pos, map_length)
    draw_food(map_len, screen, food_pos, map_length)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
