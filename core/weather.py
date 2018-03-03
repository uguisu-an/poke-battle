import core.type as t


def adjust(weather, move):
    if weather in ['Sunny', 'Drought']:
        if move.type == t.Fire:
            move.power *= 1.5
        if move.type == t.Water:
            if weather == 'Sunny':
                move.power *= 0.5
            if weather == 'Drought':
                move.power = 0
        if move.name == 'Weather Ball':
            move.power *= 2.0
            move.type = t.Fire
    if weather in ['Rain', 'Heavy Rain']:
        if move.type == t.Fire:
            if weather == 'Rain':
                move.power *= 0.5
            if weather == 'Heavy Rain':
                move.power = 0
        if move.type == t.Water:
            move.power *= 1.5
        if move.name == 'Solar Beam':
            move.power *= 0.5
        if move.name == 'Weather Ball':
            move.power *= 2.0
            move.type = t.Water
    if weather == 'Hail':
        if move.name == 'Solar Beam':
            move.power *= 0.5
        if move.name == 'Weather Ball':
            move.power *= 2.0
            move.type = t.Ice
