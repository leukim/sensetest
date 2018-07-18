from sense_hat import SenseHat
from time import sleep

from Board import Board

game_active = True
board = Board()

sense = SenseHat()
sense.set_rotation(90)

while True:
    if game_active:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'middle':
                    board.select_current_cell()
                else:
                    board.selector.move(event.direction)

        sense.set_pixels(board.to_pixel_array())
        sleep(0.1)
        winner = board.state.get_winner()
        if winner is not None:
            sense.clear(winner)
            sleep(1)
            game_active = False
    else:
        for event in sense.stick.get_events():
            if event.action == 'pressed' and event.direction == 'middle':
                board = Board()
        game_active = True
