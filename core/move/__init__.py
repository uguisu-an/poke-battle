from functools import reduce
from operator import mul
from core.effect.weather import *


class Attack:
    name = ''
    type = None
    power = 0

    # タイプ一致の判定
    def type_match(self, *types):
        return any(t_ == self.type for t_ in types)

    # タイプ一致による補正値
    def type_match_bonus(self, *types):
        if self.type_match(*types):
            return 1.2
        return 1.0

    # タイプ相性による補正値
    def type_match_up(self, *types):
        return reduce(mul, (self.type.affect(t_) for t_ in types))

    # TODO: 操作に依存させる
    def affected_by(self, weather):
        if weather == Sunny:
            if self.type == t.Fire:
                self.power *= 1.5
            if self.type == t.Water:
                self.power *= 0.5
        if weather == Drought:
            if self.type == t.Fire:
                self.power *= 1.5
            if self.type == t.Water:
                self.power = 0
        if weather == Rainy:
            if self.type == t.Water:
                self.power *= 1.5
            if self.type == t.Fire:
                self.power *= 0.5
        if weather == HeavyRainy:
            if self.type == t.Water:
                self.power *= 1.5
            if self.type == t.Fire:
                self.power = 0


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
