def base_damage(a, b):
    return a['level'].correct(a['move'].damage(a, b)) / 50 + 2

