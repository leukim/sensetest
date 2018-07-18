class Cell:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def as_array(self):
        return [self.r, self.g, self.b]
