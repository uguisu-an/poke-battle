import random


# attack-moveに計算させてもいい
def base_damage(power, attack_defence_ratio):
    return power * attack_defence_ratio + 2


def _default_randomizer(minimum, maximum):
    return random.choice(range(minimum, maximum + 1))


# 乱数を与える
def randomized(damage, randomizer=_default_randomizer):
    return damage * (randomizer(85, 100) / 100)
