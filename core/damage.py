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
    critical = False

    def __init__(self, move, attacker, defender):
        self.move: Attack = move
        self.add_attacker(attacker)
        self.add_defender(defender)

    def add_attacker(self, attacker: Monster):
        self.attacker = attacker
        self.attacker_character = attacker.character
        self.attacker_item = attacker.item

    def add_defender(self, defender: Monster):
        self.defender = defender
        self.defender_character = defender.character
        self.defender_item = defender.item

    def add_randomizer(self, randomizer):
        self.randomizer = randomizer

    def calc_base_damage(self):
        return base_damage(self.move.power, self._calc_attack_defence_ratio())

    def _calc_attack_defence_ratio(self):
        return self.attacker.attack(self.move) / self.defender.defend(self.move)

    def calc_item_bonus(self):
        return self._calc_attacker_item_bonus() * self._calc_defender_item_bonus()

    def _calc_attacker_item_bonus(self):
        if self.attacker_item == LifeOrb:
            return 1.3
        if self.attacker_item == ExpertBelt:
            return 1.2
        return 1.0

    def _calc_defender_item_bonus(self):
        if self.defender_item == Berry:
            return 0.5
        return 1.0

    def calc_character_bonus(self):
        return self._calc_attacker_character_bonus() * self._calc_defender_character_bonus()

    def _calc_attacker_character_bonus(self):
        if self.attacker_character == BrainForce and self.move.type_match_up(self.defender.type) > 1:
            return 1.2
        if self.attacker_character == TintedLens and self.move.type_match_up(self.defender.type) < 1:
            return 2.0
        if self.attacker_character == Sniper and self.critical:
            return 1.5
        return 1.0

    def _calc_defender_character_bonus(self):
        if self.defender_character in {HardRock, Filter} and self.move.type_match_up(self.defender.type) > 1:
            return 0.75
        if self.defender_character in {Multiscale, PhantomGuard} and self.attacker.hp == self.attacker.max_hp:
            return 0.5
        return 1.0

    def calc_critical_bonus(self):
        if self.critical:
            return 2.0
        return 1.0

    def calc(self):
        damage = self.calc_base_damage()
        damage = randomized(damage, randomizer=self.randomizer)
        damage = damage * self.move.type_match_bonus(self.attacker.type)
        damage = damage * self.move.type_match_up(self.defender.type)
        damage = damage * self.calc_item_bonus()
        damage = damage * self.calc_character_bonus()
        damage = damage * self.calc_critical_bonus()
        return damage
