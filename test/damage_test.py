import core.type as t
from core.move import *
from core.level import Level
from core.damage import *
from core.monster import Monster


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


def test_level_adjust_attack():
    assert Level(1).adjust(1) == 2.4
    assert Level(10).adjust(1) == 6.0
    assert Level(50).adjust(1) == 22.0


def test_base_damage():
    assert base_damage(120, 1.0) == 122
    assert base_damage(120, 2.0) == 242


def test_type_match():
    move = Attack()
    move.type = t.Normal
    assert move.type_match(t.MonsterType(t.Normal))
    assert not move.type_match(t.MonsterType(t.Dragon))


def test_type_match_up():
    move = Attack()
    move.type = t.Ground
    assert move.type_match_up(t.MonsterType(t.Fire, t.Flying)) == 0
    assert move.type_match_up(t.MonsterType(t.Fire, t.Grass)) == 1.0
    assert move.type_match_up(t.MonsterType(t.Fire, t.Electric)) == 4.0


def test_randomized_damage():
    get_minimum = (lambda m, _: m)
    get_maximum = (lambda _, n: n)
    assert randomized(100, randomizer=get_minimum) == 85
    assert randomized(100, randomizer=get_maximum) == 100
