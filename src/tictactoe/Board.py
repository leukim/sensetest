from copy import deepcopy

from Colour import Colour
from State import State
from Selector import Selector


class Board:
    GAME_CELL_TO_BOARD_PIXELS = [
        [[[0, 0], [0, 1], [1, 0], [1, 1]], [[3, 0], [3, 1], [4, 0], [4, 1]], [[6, 0], [6, 1], [7, 0], [7, 1]]],
        [[[0, 3], [1, 3], [0, 4], [1, 4]], [[3, 3], [3, 4], [4, 3], [4, 4]], [[6, 3], [6, 4], [7, 3], [7, 4]]],
        [[[0, 6], [0, 7], [1, 6], [1, 7]], [[3, 6], [3, 7], [4, 6], [4, 7]], [[6, 6], [6, 7], [7, 6], [7, 7]]]
    ]

    def __init__(self):
        _ = Colour.BLACK
        W = Colour.WHITE

        self.board = [
            [_, _, W, _, _, W, _, _],
            [_, _, W, _, _, W, _, _],
            [W, W, W, W, W, W, W, W],
            [_, _, W, _, _, W, _, _],
            [_, _, W, _, _, W, _, _],
            [W, W, W, W, W, W, W, W],
            [_, _, W, _, _, W, _, _],
            [_, _, W, _, _, W, _, _],
        ]

        self.state = State()

        self.selector = Selector()

    def select_current_cell(self):
        if self.state.get_cell(self.selector.x, self.selector.y) == Colour.BLACK:
            self.state.set_cell(self.selector.x, self.selector.y, self.state.current_player)
            self.state.switch_player()

    def to_pixel_array(self):
        _board = deepcopy(self.board)

        self.__insert_selector(_board)

        self.__insert_state(_board)

        array = []
        for row in _board:
            for cell in row:
                array.append(cell.as_array())
        return array

    def __insert_selector(self, _board):
        for cell in Board.GAME_CELL_TO_BOARD_PIXELS[self.selector.x][self.selector.y]:
            if self.state.current_player == Colour.RED:
                _board[cell[0]][cell[1]] = Colour.DIM_RED
            else:
                _board[cell[0]][cell[1]] = Colour.DIM_BLUE

    def __insert_state(self, _board):
        for x in range(3):
            for y in range(3):
                if self.state.get_cell(x, y) != Colour.BLACK:
                    for cell in Board.GAME_CELL_TO_BOARD_PIXELS[self.selector.x][self.selector.y]:
                        _board[cell[0]][cell[1]] = self.state.get_cell(x, y)
