class Stat:
    def __init__(self, degree):
        self._degree = degree
        self.rank = Rank(0)

    @property
    def degree(self):
        return self.rank.adjust(self._degree)

    def __eq__(self, other):
        return self.degree == other


class Rank:
    MINIMUM = -6
    MAXIMUM = +6

    def __init__(self, rank=0):
        assert Rank.MINIMUM <= rank <= Rank.MAXIMUM
        self._rank = rank

    @property
    def rate(self):
        a = 2
        b = 2
        if self._rank > 0:
            a += self._rank
        if self._rank < 0:
            b -= self._rank
        return a / b

    def adjust(self, stat):
        return stat * self.rate

    def up(self):
        if self._rank >= self.MAXIMUM:
            return
        self._rank += 1

    def down(self):
        if self._rank <= self.MINIMUM:
            return
        self._rank -= 1
