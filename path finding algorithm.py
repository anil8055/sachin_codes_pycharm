import pygame
from math import sqrt

pygame.init()
win_size = 600
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption('path finding algorithm')
row = 50
gap = win_size // row
stop = False
paint = False
start_end = []
start_path_finding = False
path_found = False
clock = pygame.time.Clock()
black_box = []


def draw_grid():
    win.fill((150, 150, 100))
    i = 0
    for x in range(row):
        pygame.draw.line(win, (255, 255, 255), (0, i), (win_size, i))
        pygame.draw.line(win, (255, 255, 255), (i, 0), (i, win_size))
        i += gap


def draw_rect(position, color):
    if color == 1:
        pygame.draw.rect(win, (0, 0, 0), ((position[0] // gap) * gap, (position[1] // gap) * gap, gap - 1, gap - 1))
    elif color == 2:
        pygame.draw.rect(win, (255, 0, 0), ((position[0] // gap) * gap, (position[1] // gap) * gap, gap - 1, gap - 1))
    elif color == 3:
        pygame.draw.rect(win, (150, 255, 150),
                         (position[0] * gap, position[1] * gap, gap - 1, gap - 1))
    else:
        pygame.draw.rect(win, (255, 255, 0), (position[0] * gap, position[1] * gap, gap - 1, gap - 1))
    pygame.display.update()


def distance(starting_coordinates, ending_coordinate):
    if starting_coordinates == start_end[0] or starting_coordinates == start_end[1]:
        pass
    else:
        draw_rect(starting_coordinates, 3)
    return abs(sqrt(((ending_coordinate[0] - starting_coordinates[0]) ** 2) + (
            (ending_coordinate[1] - starting_coordinates[1]) ** 2)))


def path_finder():
    start = start_end[0]
    end = start_end[1]
    current_node = start
    path_array = []
    while not path_found:
        up = distance([current_node[0], current_node[1] - 1], end)
        down = distance([current_node[0], current_node[1] + 1], end)
        left = distance([current_node[0] - 1, current_node[1]], end)
        right = distance([current_node[0] + 1, current_node[1]], end)
        temporary_dict = {up: [current_node[0], current_node[1] - 1],
                          down: [current_node[0], current_node[1] + 1],
                          left: [current_node[0] - 1, current_node[1]],
                          right: [current_node[0] + 1, current_node[1]]}
        array = [left, right, up, down]
        current_node = temporary_dict[min(array)]
        if current_node == end:
            break
        path_array.append(current_node)
        clock.tick(10)
    for x in path_array:
        draw_rect(x, 4)


draw_grid()
while not stop:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            win = True
            pygame.quit()
            exit()
        # to set events for mouse to draw boxes
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                paint = True
            elif event.button == 3:
                if len(start_end) < 2:
                    draw_rect(pos, 2)
                    start_end.append([pos[0] // gap, pos[1] // gap])
                else:
                    path_finder()
        if event.type == pygame.MOUSEBUTTONUP:
            paint = False

    # to draw the black box on board
    if paint:
        draw_rect(pos, 1)
        # to store the position of the boxes which are black
        black_box_coordinates = [pos[0] // gap, pos[1] // gap]
        if not (black_box_coordinates in black_box):
            black_box.append(black_box_coordinates)
    else:
        pass
    pygame.display.update()
