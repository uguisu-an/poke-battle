import core.type as t


def adjust(weather, move):
    if weather == 'Sunny':
        if move.type == t.Fire:
            move.power *= 1.5
        if move.type == t.Water:
            move.power *= 0.5
        if move.name == 'Weather Ball':
            move.power *= 2.0
            move.type = t.Fire
    if weather == 'Rain':
        if move.type == t.Fire:
            move.power *= 0.5
        if move.type == t.Water:
            move.power *= 1.5
        if move.name == 'Solar Beam':
            move.power *= 0.5
        if move.name == 'Weather Ball':
            move.power *= 2.0
            move.type = t.Water


