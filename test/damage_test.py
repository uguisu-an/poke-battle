import core.type as t
from core.move import NormalMove, SpecialMove
from core.level import Level
from core.damage import base_damage, type_effect


def setup():
    global a, b
    a = {
        'level': Level(50),
        'types': [],
        'atk': 150,
        'sp.atk': 150,
    }
    b = {
        'level': Level(50),
        'types': [],
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


def test_damage_same_type_bonus():
    a['types'] = [t.Normal]
    b['types'] = [t.Water, t.Fire]
    assert type_effect(NormalMove(move_type=t.Normal), a, b) == 1.2
    assert type_effect(SpecialMove(move_type=t.Electric), b, a) == 1.0


def test_damage_water_type_chemistry():
    b['types'] = [t.Water]
    assert type_effect(NormalMove(move_type=t.Water), a, b) == 0.5
    b['types'] = [t.Fire, t.Water]
    assert type_effect(NormalMove(move_type=t.Water), a, b) == 1.0


def test_damage_dragon_type_chemistry():
    b['types'] = [t.Dragon]
    assert type_effect(NormalMove(move_type=t.Dragon), a, b) == 2.0
    b['types'] = [t.Dragon, t.Fairy]
    assert type_effect(NormalMove(move_type=t.Dragon), a, b) == 0


