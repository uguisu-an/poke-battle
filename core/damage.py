def level_revision(level):
    return level * 2 / 5 + 2


def base_damage(a, b):
    return a['move'].damage(a, b) * level_revision(a['level']) / 50 + 2

