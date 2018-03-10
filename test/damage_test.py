from importlib import reload
import core.damage2 as d2


def setup():
    reload(d2)


def test_default_setup():
    assert d2.calc() == 54


def test_base_damage():
    d2.at_stat = 150
    d2.df_stat = 50
    assert d2.calc() == 160
    d2.mv_level = 1
    assert d2.calc() == 19


def test_type_match():
    d2.mv_type = d2.Type.Normal
    d2.at_type = {d2.Type.Fire, d2.Type.Normal}
    assert d2.calc() == 65


def test_type_effect():
    d2.mv_type = d2.Type.Dragon
    d2.df_type = {d2.Type.Dragon, d2.Type.Fairy}
    assert d2.calc() == 0
