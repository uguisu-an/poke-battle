class Move:
    def select_attack(self, attacker):
        return 0

    def select_defence(self, defender):
        return 0


# TODO: NoneType作る？
class NormalMove(Move):
    def __init__(self, power=0, move_type=None):
        self.power = power
        self.type = move_type

    def select_attack(self, attacker):
        return attacker['atk']

    def select_defence(self, defender):
        return defender['def']


class SpecialMove(Move):
    def __init__(self, power=0, move_type=None):
        self.power = power
        self.type = move_type

    def select_attack(self, attacker):
        return attacker['sp.atk']

    def select_defence(self, defender):
        return defender['sp.def']
