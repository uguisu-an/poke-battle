def base_damage(move, a, b):
    return a['level'].correct(move.damage(a, b)) / 50 + 2


def type_effect(move, a, b):
    effect = 1
    for type_ in a['types']:
        effect *= move.type.boost(type_)
    return effect
