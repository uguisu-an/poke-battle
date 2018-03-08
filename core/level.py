class Level:
    def __init__(self, level):
        self.level = level

    def adjust(self, attack):
        return attack * (self.level * 2 / 5 + 2)

    def get_rate(self):
        return self.level * 2 / 5 + 2
