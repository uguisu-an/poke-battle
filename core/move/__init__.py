from functools import reduce
from operator import mul


class Attack:
    name = ''
    type = None
    power = 0

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
