import random
from core.move import Attack
from core.monster import Monster


# attack-moveに計算させてもいい
def base_damage(power, attack_defence_ratio):
    return power * attack_defence_ratio + 2


def default_randomizer(minimum, maximum):
    return random.choice(range(minimum, maximum + 1))


def minimizer(minimum, _):
    return minimum


def maximizer(_, maximum):
    return maximum


# 乱数を与える
def randomized(damage, randomizer=default_randomizer):
    return damage * (randomizer(85, 100) / 100)


class DamageCalculator:
    randomizer = default_randomizer

    def __init__(self):
        self.move: Attack = None
        self.attacker: Monster = None
        self.defender: Monster = None

    def add_randomizer(self, randomizer):
        self.randomizer = randomizer

    def calc_base_damage(self):
        return base_damage(self.move.power, self.calc_attack_defence_ratio())

    def calc_attack_defence_ratio(self):
        return self.attacker.attack(self.move) / self.defender.defend(self.move)

    def calc(self):
        damage = self.calc_base_damage()
        damage = randomized(damage, randomizer=self.randomizer)
        damage = damage * self.move.type_match_bonus(self.attacker.type)
        damage = damage * self.move.type_match_up(self.defender.type)
        return damage
