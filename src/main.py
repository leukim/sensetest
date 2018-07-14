import time
from sense_hat import SenseHat


def tick():
    pass


if __name__ == '__main__':
    sense = SenseHat()

    sense.show_message("Hello world!")
    print "HELLO WORLD"

    starttime = time.time()
    while True:
        tick()
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))
