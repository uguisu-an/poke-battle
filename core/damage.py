def base_damage(move, a, b):
    return a['level'].correct(move.damage(a, b)) / 50 + 2

