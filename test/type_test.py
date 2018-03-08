import core.type as t


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
