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