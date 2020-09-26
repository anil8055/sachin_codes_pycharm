import pygame
from random import randint

win_size = 500
row = 20
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption('random selector!')
gap = win_size // row
grid_size = gap


# drawing the selection box for selecting player


def num_generate(player_num):
    random_number = []
    ret_array = []
    for x in range(player_num):
        random_number.append(randint(10, 30))
        ret_array[x][1] = array[x][1] - rand_list[x]
    return array
    return random_number


def render_message(message_number):
    font = pygame.font.SysFont('comicsansms', 28)
    if message_number == 1:
        message = font.render('invalid player number', True, (255, 25, 40))
        win.blit(message, (100, 240))

    elif message_number == 2:
        font = pygame.font.SysFont('freelansbold', 25)
        y_axis = start_point
        for x in range(player):
            message = font.render(str(ranking[x][0] + 1), True, (255, 0, 0))
            win.blit(message, (ranking[x][1], y_axis))
            y_axis += gap
            pygame.display.update()


def draw_grid(space):
    win.fill((255, 255, 255))
    while space <= win_size:
        pygame.draw.line(win, (0, 0, 0), (0, space), (win_size, space))
        pygame.draw.line(win, (0, 0, 0), (space, 0), (space, win_size))
        space += grid_size


def initialize_blocks(player_num):
    array = [[start_point + (x * gap) + 1, 18 * gap + 1] for x in range(player_num)]
    i = 0
    for x in array:
        pygame.draw.rect(win, color_list[i], (x[0], x[1], gap - 1, gap - 1))
        i += 1
    print(array)
    return array


def increase(rand_list, array):



def draw_pieces(array, final_array):
    i = 0
    for x in range(len(array)):
        array[x][1] += final_array[x]
        if array[x][0] <= gap:
            pygame.draw.rect(win, color_list[i], (array[x][0], gap - 1, gap - 1, gap - 1))
            i += 1
        else:
            pygame.draw.rect(win, color_list[i], (array[x][0], array[x][1], gap - 1, (final_array[x] - array[x][0])))
            i += 1
    clock.tick(3)


def winner_list(array):
    for x in range(len(array)):
        if array[x][1] <= gap:
            if [x, array[x][0]] in ranking:
                continue
            ranking.append([x, array[x][0]])
    return ranking


def initializing_player_number():
    player_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    font = pygame.font.SysFont('comicsansms', 28)
    i = 4
    j = 5
    for x in range(19):
        pygame.draw.circle(win, (255, 0, 0), (i * gap, j * gap), 20, 20)
        if i >= 15:
            i = 4
            j += 3
        else:
            i += 3


def play():
    winner = False

    draw_grid(gap)
    position_of_player = initialize_blocks(player)
    while not winner:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                exit()
        # initializing_player_number()
        if start:
            if player > 20 or player < 1:
                render_message(1)
            winner_list(position_of_player)
            if len(ranking) == player:
                render_message(2)
                print(ranking)
            number = num_generate(player)
            position_of_player = increase(number, position_of_player)
            draw_pieces(position_of_player, number)

        pygame.display.update()


color_list = [(255, 102, 255), (178, 102, 255), (102, 178, 255), (102, 255, 178), (178, 255, 102),
              (255, 178, 102), (128, 255, 0), (0, 255, 128), (76, 0, 153), (96, 96, 96),
              (102, 102, 0), (229, 255, 204), (25, 0, 51), (102, 51, 0), (0, 0, 0),
              (1, 104, 63), (255, 145, 0), (255, 239, 0), (102, 51, 51), (145, 255, 0)]
player = 5
start_point = (10 - (player // 2)) * gap
start = True
ranking = []
play()
