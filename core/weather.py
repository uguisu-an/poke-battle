import core.type as t


# def adjust_accuracy(weather, move):
#     accuracy = 1.0
#     if weather == 'Sunny':
#         if move == 'Thunder' or move == 'Hurricane':
#             accuracy *= 0.5
#     return accuracy


def adjust(weather, damage, damage_type):
    if weather == 'Sunny':
        if damage_type == t.Fire:
            damage *= 1.5
        if damage_type == t.Water:
            damage *= 0.5
    if weather == 'Rain':
        if damage_type == t.Fire:
            damage *= 0.5
        if damage_type == t.Water:
            damage *= 1.5
    return damage


