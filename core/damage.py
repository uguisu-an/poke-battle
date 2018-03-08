import random


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
