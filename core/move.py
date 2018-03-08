from functools import reduce
from operator import mul


class Attack:
    type = None

    # タイプ一致の判定
    def type_match(self, *types):
        return any(t == self.type for t in types)

    # タイプ一致による補正値
    def type_match_bonus(self, *types):
        if self.type_match(*types):
            return 1.2
        return 1.0

    # タイプ相性による補正値
    def type_match_up(self, *types):
        return reduce(mul, (self.type.affect(t) for t in types))


class PhysicalAttack(Attack):
    @staticmethod
    def select_attack(attacker):
        return attacker.py_atk

    @staticmethod
    def select_defence(defender):
        return defender.py_def


class SpecialAttack(Attack):
    @staticmethod
    def select_attack(attacker):
        return attacker.sp_atk

    @staticmethod
    def select_defence(defender):
        return defender.sp_def


class Move:
    def select_attack(self, attacker):
        return 0

    def select_defence(self, defender):
        return 0


# TODO: NoneType作る？
class NormalMove(Move):
    def __init__(self, power=0, move_type=None, name=''):
        self.name = name
        self.power = power
        self.type = move_type

    def select_attack(self, attacker):
        return attacker['atk']

    def select_defence(self, defender):
        return defender['def']


class SpecialMove(Move):
    def __init__(self, power=0, move_type=None, name=''):
        self.name = name
        self.power = power
        self.type = move_type

    def select_attack(self, attacker):
        return attacker['sp.atk']

    def select_defence(self, defender):
        return defender['sp.def']
