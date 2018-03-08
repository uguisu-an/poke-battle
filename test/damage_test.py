import core.type as t
from core.move import *
from core.level import Level
from core.damage import *


def test_base_damage():
    assert base_damage(120, 1.0) == 122
    assert base_damage(120, 2.0) == 242


def test_type_match():
    move = Attack()
    move.type = t.Normal
    assert move.type_match(t.Normal)
    assert not move.type_match(t.Dragon)


def test_type_match_up():
    move = Attack()
    move.type = t.Ground
    assert move.type_match_up(t.Fire, t.Flying) == 0
    assert move.type_match_up(t.Fire, t.Grass) == 1.0
    assert move.type_match_up(t.Fire, t.Electric) == 4.0


def test_randomized_damage():
    get_minimum = (lambda m, _: m)
    get_maximum = (lambda _, n: n)
    assert randomized(100, randomizer=get_minimum) == 85
    assert randomized(100, randomizer=get_maximum) == 100
