class Rank:
    def __init__(self, rank=0):
        self._rank = rank

    def ratio(self):
        a = 2
        b = 2
        if self._rank > 0:
            a += self._rank
        if self._rank < 0:
            b -= self._rank
        return a / b

    def up(self):
        if self._rank >= 6:
            return
        self._rank += 1

    def down(self):
        if self._rank <= -6:
            return
        self._rank -= 1
