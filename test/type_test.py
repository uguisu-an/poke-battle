import core.type as t
from core.move import SpecialAttack
from core.move.factory import MoveBuilder
from core.effect import *


def test_type_equality():
    assert t.Normal == t.Normal
    assert t.Normal != t.Fighting


def test_normal_type_chemistry():
    assert t.Normal.affect(t.Rock) == 0.5
    assert t.Normal.affect(t.Steel) == 0.5
    assert t.Normal.affect(t.Ghost) == 0


def test_dragon_type_chemistry():
    assert t.Dragon.affect(t.Normal) == 1.0
    assert t.Dragon.affect(t.Dragon) == 2.0
    assert t.Dragon.affect(t.Steel) == 0.5
    assert t.Dragon.affect(t.Fairy) == 0


def test_inverse_battle():
    move = SpecialAttack()
    move.type = t.Dragon
    assert move.type_match_up(t.Fairy) == 0
    ib = MoveBuilder()
    ib.add_effect(InverseBattle)
    ib.build(move)
    assert move.type_match_up(t.Fairy) == 2
