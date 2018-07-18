from sense_hat import SenseHat
from time import sleep
from copy import deepcopy


_ = [0, 0, 0]
W = [100, 100, 100]
R = [255, 0, 0]
B = [0, 0, 255]
SR = [50, 0, 0]
SB = [0, 0, 50]

CELLS = [
    [[[0, 0], [0, 1], [1, 0], [1, 1]], [[3, 0], [3, 1], [4, 0], [4, 1]], [[6, 0], [6, 1], [7, 0], [7, 1]]],
    [[[0, 3], [1, 3], [0, 4], [1, 4]], [[3, 3], [3, 4], [4, 3], [4, 4]], [[6, 3], [6, 4], [7, 3], [7, 4]]],
    [[[0, 6], [0, 7], [1, 6], [1, 7]], [[3, 6], [3, 7], [4, 6], [4, 7]], [[6, 6], [6, 7], [7, 6], [7, 7]]]
        ]

def matrix_to_array(matrix):
    array = []
    for row in matrix:
        for elem in row:
            array.append(elem)
    return array

def get_selector_cells(selector):
    return CELLS[selector[0]][selector[1]]

def insert_selector(_matrix, selector, current_player):
    for cell in get_selector_cells(selector):
        if current_player == R:
            _matrix[cell[0]][cell[1]] = SR
        else:
            _matrix[cell[0]][cell[1]] = SB

def insert_state(_matrix, state):
    for x in range(3):
        for y in range(3):
            if state[x][y] != _:
                for cell in get_selector_cells([x, y]):
                    _matrix[cell[0]][cell[1]] = state[x][y]

def get_new_selector_position(selector, direction):
    _selector = deepcopy(selector)
    if direction == 'right' and _selector[1] > 0:
        _selector[1] -= 1
    elif direction == 'left' and _selector[1] < 2:
        _selector[1] += 1
    elif direction == 'down' and _selector[0] < 2:
        _selector[0] += 1
    elif direction == 'up' and _selector[0] > 0:
        _selector[0] -= 1
    return _selector

def change_player(current_player):
    if current_player == R:
        return B
    return R

def game_winner(state):
    for a in range(3):
        if state[0][a] == state[1][a] and state[1][a] == state[2][a]:
            return state[0][a]
        if state[a][0] == state[a][1] and state[a][1] == state[a][2]:
            return state[a][0]
    if state[0][0] == state[1][1] and state[1][1] == state[2][2]:
        return state[0][0]
    if state[0][2] == state[1][1] and state[1][1] == state[2][0]:
        return state[0][2]
    return _

matrix = [
    [_, _, W, _, _, W, _, _],
    [_, _, W, _, _, W, _, _],
    [W, W, W, W, W, W, W, W],
    [_, _, W, _, _, W, _, _],
    [_, _, W, _, _, W, _, _],
    [W, W, W, W, W, W, W, W],
    [_, _, W, _, _, W, _, _],
    [_, _, W, _, _, W, _, _],
        ]

selector_position = [1, 1] # Start at the central cell

state = [
        [_, _, _],
        [_, _, _],
        [_, _, _]
        ]

current_player = R

game_active = True

sense = SenseHat()
sense.set_rotation(90)

while True:
    if game_active:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'middle':
                    if state[selector_position[0]][selector_position[1]] == _:
                        state[selector_position[0]][selector_position[1]] = current_player
                        current_player = change_player(current_player)
                else:
                    selector_position = get_new_selector_position(selector_position, event.direction)
        
        display_matrix = deepcopy(matrix)
        insert_selector(display_matrix, selector_position, current_player)
        insert_state(display_matrix, state)
        pixel_array = matrix_to_array(display_matrix)
        sense.set_pixels(pixel_array)
        sleep(0.1)
        winner = game_winner(state)
        if winner != _:
            sense.clear(winner)
            sleep(1)
            game_active = False
    else:
        for event in sense.stick.get_events():
            if event.action == 'pressed' and event.direction == 'middle':
                state = [
                        [_, _, _],
                        [_, _, _],
                        [_, _, _]
                        ]
        game_active = True
