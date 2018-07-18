from enum import Enum

from Cell import Cell


class Colour(Enum):
    BLACK = Cell(0, 0, 0)
    WHITE = Cell(100, 100, 100)
    RED = Cell(255, 0, 0)
    BLUE = Cell(0, 0, 255)
    DIM_RED = Cell(50, 0, 0)
    DIM_BLUE = Cell(0, 0, 50)
