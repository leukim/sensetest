from Colour import Colour


class State:

    def __init__(self):
        _ = Colour.BLACK

        self.state = [
            [_, _, _],
            [_, _, _],
            [_, _, _]
        ]

        self.current_player = Colour.RED

    def get_cell(self, x, y):
        return self.state[x][y]

    def set_cell(self, x, y, colour):
        self.state[x][y] = colour

    def switch_player(self):
        if self.current_player == Colour.RED:
            self.current_player = Colour.BLUE
        else:
            self.current_player = Colour.RED
    
    def get_winner(self):
        for a in range(3):
            if self.state[0][a] != Colour.BLACK and self.state[0][a] == self.state[1][a] and self.state[1][a] == self.state[2][a]:
                return self.state[0][a]
            if self.state[a][0] != Colour.BLACK and self.state[a][0] == self.state[a][1] and self.state[a][1] == self.state[a][2]:
                return self.state[a][0]
        if self.state[0][0] != Colour.BLACK and self.state[0][0] == self.state[1][1] and self.state[1][1] == self.state[2][2]:
            return self.state[0][0]
        if self.state[0][2] != Colour.BLACK and self.state[0][2] == self.state[1][1] and self.state[1][1] == self.state[2][0]:
            return self.state[0][2]
        return None
