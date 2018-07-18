from sense_hat import SenseHat
from time import sleep
from random import randint


sense = SenseHat()

[X_AXIS, Y_AXIS, Z_AXIS] = [1, 2, 3]
[RIGHT, LEFT, UP, DOWN] = [1, 2, 3, 4]
B = [0, 0, 0]
W = [255, 255, 255]

THRESHOLD = 0.1

def what_is_up(x, y, z):
    if x != 0:
        return X_AXIS
    if y != 0:
        return Y_AXIS
    else:
        return Z_AXIS

def get_grid(dot):
    pixels = []
    for x_index in range(8):
        for y_index in range(8):
            if x_index == dot[0] and y_index == dot[1]:
                pixels.append(W)
            else:
                pixels.append(B)
    return pixels

def get_new_dot_position(dot, dir):
    if dir == UP and dot[1] > 0:
        dot[1] -= 1
    elif dir == DOWN and dot[1] < 7:
        dot[1] += 1
    elif dir == RIGHT and dot[0] > 0:
        dot[0] -= 1
    elif dir == LEFT and dot[0] < 7:
        dot[0] += 1
    return dot

DOT_POSITION = [0, 0]

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == 'up':
                DOT_POSITION = get_new_dot_position(DOT_POSITION, RIGHT)
            elif event.direction == 'down':
                DOT_POSITION = get_new_dot_position(DOT_POSITION, LEFT)
            elif event.direction == 'right':
                DOT_POSITION = get_new_dot_position(DOT_POSITION, DOWN)
            elif event.direction == 'left':
                DOT_POSITION = get_new_dot_position(DOT_POSITION, UP)
            elif event.direction == 'middle':
                W = [randint(0, 255), randint(0, 255), randint(0, 255)]
    
    grid = get_grid(DOT_POSITION)
    sense.set_pixels(grid)
    sleep(0.1)

