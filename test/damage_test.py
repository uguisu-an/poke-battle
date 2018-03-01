from core.move import NormalMove, SpecialMove


def level_revision(level):
    return level * 2 / 5 + 2


def base_damage(a, b):
    return a['move'].damage(a, b) * level_revision(a['level']) / 50 + 2


def test_level_revision():
    assert level_revision(1) == 2.4
    assert level_revision(10) == 6.0
    assert level_revision(50) == 22.0


def test_base_damage():
    a = {'level': 50, 'atk': 150, 'move': NormalMove(120)}
    b = {'def': 100}
    assert base_damage(a, b) == 81.2


def test_base_damage_with_special_move():
    a = {'level': 50, 'sp.atk': 150, 'move': SpecialMove(120)}
    b = {'sp.def': 100}
    assert base_damage(a, b) == 81.2
