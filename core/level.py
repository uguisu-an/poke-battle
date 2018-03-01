class Level:
    def __init__(self, level):
        self.level = level

    def correct(self, damage):
        return damage * (self.level * 2 / 5 + 2)
