import random


def base_damage(move, a, b):
    return move.power * Attacker(a).make(move) / Defender(b).make(move) + 2


def type_effect(move, a, b):
    effect = 1
    for type_ in a['types']:
        effect *= move.type.boost(type_)
    for type_ in b['types']:
        effect *= move.type.affect(type_)
    return effect


def _randomize(minimum, maximum):
    return random.choice(range(minimum, maximum + 1))


def randomized(damage, randomizer=_randomize):
    return damage * (randomizer(85, 100) / 100)


class Attacker:
    def __init__(self, attacker):
        self._attacker = attacker

    def make(self, move):
        return self._adjust_by_level(self._attack_with(move))

    def _attack_with(self, move):
        return move.select_attack(self._attacker)

    def _adjust_by_level(self, attack):
        return self._attacker['level'].adjust(attack)


class Defender:
    def __init__(self, defender):
        self._defender = defender

    def make(self, move):
        return self._defend_against(move) * 50

    def _defend_against(self, move):
        return move.select_defence(self._defender)
