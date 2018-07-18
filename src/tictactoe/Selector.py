class Selector:

    def __init__(self):
        self.x = 1
        self.y = 1

    def move(self, direction):
        if direction == 'right' and self.y > 0:
            self.y -= 1
        elif direction == 'left' and self.y < 2:
            self.y += 1
        elif direction == 'down' and self.x < 2:
            self.x += 1
        elif direction == 'up' and self.x > 0:
            self.x -= 1
