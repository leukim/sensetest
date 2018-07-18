from sense_hat import SenseHat
from time import sleep
from copy import copy


sense = SenseHat()

[X_AXIS, Y_AXIS, Z_AXIS] = [1, 2, 3]
[RIGHT, LEFT, UP, DOWN] = [1, 2, 3, 4]
B = [0, 0, 0]
W = [255, 255, 255]
R = [255, 0, 0]

THRESHOLD = 0.1

def what_is_up(x, y, z):
    if x != 0:
        return X_AXIS
    if y != 0:
        return Y_AXIS
    else:
        return Z_AXIS

def get_grid(dot, painted):
    pixels = []
    for x_index in range(8):
        for y_index in range(8):
            if x_index == dot[0] and y_index == dot[1]:
                pixels.append(W)
            elif [x_index, y_index] in painted:
                pixels.append(R)
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
PAINTED_PIXELS = []

while True:
    acc = sense.get_accelerometer_raw()
    
    x = acc['x']
    y = acc['y']
    z = acc['z']
    
    x=round(x, 1)
    y=round(y, 1)
    z=round(z, 1)
    
    #up = what_is_up(x, y, z)
    
    if x > THRESHOLD or x < -THRESHOLD: #up == X_AXIS:
        if x > 0:
            DOT_POSITION = get_new_dot_position(DOT_POSITION, DOWN)
        else:
            DOT_POSITION = get_new_dot_position(DOT_POSITION, UP)
    if y > THRESHOLD or y < THRESHOLD: #up == Y_AXIS:
        if y > 0:
            DOT_POSITION = get_new_dot_position(DOT_POSITION, LEFT)
        else:
            DOT_POSITION = get_new_dot_position(DOT_POSITION, RIGHT)
    
    if DOT_POSITION not in PAINTED_PIXELS:
        PAINTED_PIXELS.append(copy(DOT_POSITION))
    
    grid = get_grid(DOT_POSITION, PAINTED_PIXELS)
    sense.set_pixels(grid)
    sleep(0.1)
