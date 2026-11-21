class Barrier:
    def __init__(self, health):
        self.health = health

    def hit(self):
        self.health = self.health - 1
        if self.health <= 0:
            print("barrier destroyed")
