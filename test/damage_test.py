from core.move import NormalMove, SpecialMove
from core.level import Level
from core.damage import base_damage


def setup():
    global a, b
    a = {
        'level': Level(50),
        'atk': 150,
        'sp.atk': 150,
    }
    b = {
        'level': Level(50),
        'def': 100,
        'sp.def': 100,
    }


def test_level_revision():
    assert Level(1).correct(1) == 2.4
    assert Level(10).correct(1) == 6.0
    assert Level(50).correct(1) == 22.0


def test_base_damage():
    move = NormalMove(120)
    assert base_damage(move, a, b) == 81.2


def test_base_damage_with_special_move():
    move = SpecialMove(120)
    assert base_damage(move, a, b) == 81.2

