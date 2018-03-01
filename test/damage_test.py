from core.move import NormalMove, SpecialMove
from core.damage import level_revision, base_damage


def setup():
    global a, b
    a = {
        'level': 50,
        'atk': 150,
        'sp.atk': 150,
    }
    b = {
        'level': 50,
        'def': 100,
        'sp.def': 100,
    }


def test_level_revision():
    assert level_revision(1) == 2.4
    assert level_revision(10) == 6.0
    assert level_revision(50) == 22.0


def test_base_damage():
    a['move'] = NormalMove(120)
    assert base_damage(a, b) == 81.2


def test_base_damage_with_special_move():
    a['move'] = SpecialMove(120)
    assert base_damage(a, b) == 81.2

