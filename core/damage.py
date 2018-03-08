import random


# attack-moveに計算させてもいい
def base_damage(power, attack_defence_ratio):
    return power * attack_defence_ratio + 2


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
