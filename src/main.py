from sense_hat import SenseHat
from time import sleep
from random import randint

[X_AXIS, Y_AXIS, Z_AXIS] = [1, 2, 3]
B = [0, 0, 0]
W = [255, 255, 255]

def what_is_up(x, y, z):
    if x != 0:
        return X_AXIS
    if y != 0:
        return Y_AXIS
    else:
        return Z_AXIS

ARROW_UP = [
    B, B, B, W, W, B, B, B,
    B, B, W, W, W, W, B, B,
    B, W, W, W, W, W, W, B,
    W, W, W, W, W, W, W, W,
    B, B, B, W, W, B, B, B,
    B, B, B, W, W, B, B, B,
    B, B, B, W, W, B, B, B,
    B, B, B, W, W, B, B, B,
           ]

POINT = [
    B, B, B, W, W, B, B, B,
    B, B, W, W, W, W, B, B,
    B, W, W, B, B, W, W, B,
    W, W, B, B, B, B, W, W,
    W, W, B, B, B, B, W, W,
    B, W, W, B, B, W, W, B,
    B, B, W, W, W, W, B, B,
    B, B, B, W, W, B, B, B,
           ]

random_colour = [randint(0, 255), randint(0, 255), randint(0, 255)]

sense = SenseHat()
sense.set_rotation(180)

##while True:
##    pressure = sense.get_pressure()
##    temp = sense.get_temperature()
##    humidity = sense.get_humidity()
##    print(pressure)
##    print(temp)
##    print(humidity)
##    
##    info = "%.1f C %.1f%% %.0f" % (temp, humidity, pressure)
##    
##    sense.show_message(info)
##    sleep(1)

while True:
    o = sense.get_orientation()
    
##    pitch = o["pitch"]
##    roll = o["roll"]
##    yaw = o["yaw"]
##    print("Pitch: %.4f Roll: %.4f Yaw: %.4f" % (pitch, roll, yaw))
    acc = sense.get_accelerometer_raw()
    
    x = acc['x']
    y = acc['y']
    z = acc['z']
    
    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)
    
    up = what_is_up(x, y, z)
    
    if up == X_AXIS:
        if x > 0:
            sense.set_rotation(270)
        else:
            sense.set_rotation(90)
        sense.set_pixels(ARROW_UP)
    elif up == Y_AXIS:
        if y > 0:
            sense.set_rotation(0)
        else:
            sense.set_rotation(180)
        sense.set_pixels(ARROW_UP)
    else:
        sense.set_pixels(POINT)
    
    print("X: %d Y: %d Z: %d" % (x, y, z))

sense.clear()