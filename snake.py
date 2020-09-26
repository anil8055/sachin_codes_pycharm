import pygame
import time

pygame.init()
screen_width = 500
row = 20
win = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('simple snake game')
playing = True
gap = screen_width // row
snake_size = gap
x_coordinate = screen_width // 2
y_coordinate = screen_width // 2
x_change = 0
y_change = 0
snake_position = [[x_coordinate, y_coordinate]]


def draw_board():
    global gap, snake_size, screen_width
    win.fill((0, 0, 0))
    while gap <= screen_width:
        pygame.draw.line(win, (255, 255, 255), (0, gap), (screen_width, gap))
        pygame.draw.line(win, (255, 255, 255), (gap, 0), (gap, screen_width))
        gap += snake_size
        # pygame.draw.rect(win, (255, 0, 0), (snake_position[0][0], snake_position[0][1], snake_size, snake_size))
        pygame.display.update()
    return


while playing:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            playing = False
            pygame.quit()
            quit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_DOWN:
                y_change = snake_size
                x_change = 0
            if events.key == pygame.K_UP:
                y_change = -snake_size
                x_change = 0
            if events.key == pygame.K_RIGHT:
                x_change = snake_size
                y_change = 0
            if events.key == pygame.K_LEFT:
                x_change = -snake_size
                y_change = 0
    x_coordinate += x_change
    y_coordinate += y_change
    snake_position.insert(0, [x_coordinate, y_coordinate])
    snake_position.pop()
    draw_board()
    pygame.draw.rect(win, (255, 0, 0), (snake_position[0][0], snake_position[0][1], snake_size - 1, snake_size - 1))
    time.sleep(0.1)
    pygame.display.update()
