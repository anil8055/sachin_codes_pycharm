import pygame
from random import randint, choice
import threading
import time
import numpy as np
import pyastar

pygame.init()
screen_x = 800
screen_y = 400
win = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('maze creator')
end_programme = False
column = 50
gap = screen_x // column
paint = False
start_end = []
black_box = []
clock = pygame.time.Clock()


def draw_grid():
    win.fill((150, 150, 100))
    i = 0
    rows = 0
    for x in range(column):
        if i <= screen_y:
            pygame.draw.line(win, (255, 255, 255), (0, i), (screen_x, i))  # to print horizontal lines
            rows += 1
        if i <= screen_x:
            pygame.draw.line(win, (255, 255, 255), (i, 0), (i, screen_y))  # to print vertical lines
        i += gap
    pygame.display.update()
    return rows


def draw_rect(position, color):
    if color == 1:
        pygame.draw.rect(win, (0, 0, 0), (position[0] * gap, position[1] * gap, gap - 1, gap - 1))
    elif color == 2:
        pygame.draw.rect(win, (255, 20, 147), ((position[0] // gap) * gap,
                                               (position[1] // gap) * gap, gap - 1, gap - 1))
    elif color == 3:
        pygame.draw.rect(win, (150, 255, 150),
                         (position[0] * gap, position[1] * gap, gap - 1, gap - 1))
    else:
        pygame.draw.rect(win, (255, 255, 0), (position[0] * gap, position[1] * gap, gap - 1, gap - 1))
    pygame.display.update()


def make_obstacles():
    array = ['left', 'right', 'up', 'down']
    for x in range(column):
        current_node = [randint(0, column), randint(0, row)]
        if current_node in black_box:
            continue
        direction_to_draw = choice(array)
        for y in range(randint(3, 7)):
            direction = {'right': [current_node[0] + 1, current_node[1]],
                         'left': [current_node[0] - 1, current_node[1]],
                         'up': [current_node[0], current_node[1] - 1],
                         'down': [current_node[0], current_node[1] + 1]}
            next_node = direction[direction_to_draw]
            if next_node in black_box:
                break
            black_box.append(next_node)
            draw_rect(next_node, 1)
            if 0 <= next_node[0] < column and 0 <= next_node[1] < row:
                current_node = next_node
            else:
                break
            # clock.tick(5)
            time.sleep(0.2)
            pygame.display.update()


'''class State(object):
    def __init__(self, value, parent, start=0, goal=0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0

        if parent:
            self.start = parent.start
            self.goal = parent.goal
            self.path = parent.path[:]
            self.path.append(value)
        else:
            self.path = [value]
            self.start = start
            self.goal = goal


class StateString(State):
    def __init__(self, value, parent, start=0, goal=0):
        super(StateString, self).__init__(value, parent, start, goal)
        self.dist = self.get_distance()

    def get_distance(self):
        if self.value == self.goal:
            return 0
        dist = 0

        for i in range(len(self.goal)):
            letter = self.goal[i]

            dist += abs(i - self.value.index(letter))
        return dist

    def create_children(self):

        if not self.children:
            for i in range(len(
                    self.goal) - 1):
                val = self.value
                val = val[:i] + val[i + 1] + val[i] + val[i + 2:]
                child = StateString(val, self)
                self.children.append(child)'''


row = draw_grid()
t = threading.Thread(target=make_obstacles(), name='make_obtacle', args=())
t.start()
# make_obstacles()
while not end_programme:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_programme = True
            pygame.quit()
            exit()

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
        draw_rect([pos[0] // gap, pos[1] // gap], 1)
        # to store the position of the boxes which are black
        if [pos[0] // gap, pos[1] // gap] not in black_box:
            black_box.append([pos[0] // gap, pos[1] // gap])
    pygame.display.update()
