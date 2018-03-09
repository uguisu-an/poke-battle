import random
from core.move import Attack
from core.monster import Monster
from core.item import *
from core.character import *


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
    attacker = None
    attacker_item = None
    attacker_character = None
    defender = None
    defender_item = None
    defender_character = None

    def __init__(self, move, attacker, defender):
        self.move: Attack = move
        self.add_attacker(attacker)
        self.add_defender(defender)

    def add_attacker(self, monster):
        self.attacker = monster
        self.add_attacker_character(monster.character)
        self.add_attacker_item(monster.item)

    def add_defender(self, monster):
        self.defender = monster
        self.defender_character(monster.character)
        self.defender_item(monster.item)

    def add_randomizer(self, randomizer):
        self.randomizer = randomizer

    def add_attacker_item(self, item):
        self.attacker_item = item

    def add_defender_item(self, item):
        self.defender_item = item

    def add_attacker_character(self, character):
        self.attacker_character = character

    def add_defender_character(self, character):
        self.defender_character = character

    def calc_base_damage(self):
        return base_damage(self.move.power, self.calc_attack_defence_ratio())

    def calc_attack_defence_ratio(self):
        return self.attacker.attack(self.move) / self.defender.defend(self.move)

    def calc_item_bonus(self):
        if self.defender_item == Berry:
            return 0.5
        return 1.0

    def calc_character_bonus(self):
        if self.attacker_character == BrainForce and self.move.type_match_up(self.defender.type) > 1:
            return 1.2
        return 1.0

    def calc(self):
        damage = self.calc_base_damage()
        damage = randomized(damage, randomizer=self.randomizer)
        damage = damage * self.move.type_match_bonus(self.attacker.type)
        damage = damage * self.move.type_match_up(self.defender.type)
        damage = damage * self.calc_item_bonus()
        damage = damage * self.calc_character_bonus()
        return damage
