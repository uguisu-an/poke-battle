from core.stat import *
from core.monster import *
from core.item import *
from core.stat_builder import *


def test_level_rate():
    assert Level(1).get_rate() == 2.4
    assert Level(10).get_rate() == 6.0
    assert Level(50).get_rate() == 22.0


def test_stat():
    atk = Stat(100)
    assert atk == 100
    atk.rank.up()
    assert atk == 150
    atk.rank.down()
    assert atk == 100


def test_rank_adjust_stat():
    assert Rank(0).adjust(100) == 100
    assert Rank(6).adjust(100) == 400
    assert Rank(-6).adjust(100) == 25


def test_rank_up_limit():
    rank = Rank(6)
    rank.up()
    assert rank.adjust(100) == 400


def test_rank_down_limit():
    rank = Rank(-6)
    rank.down()
    assert rank.adjust(100) == 25


# ごちゃごちゃしてる
def test_defeatist():
    base = Monster(hp=100, py_atk=20, sp_atk=30)
    builder = StatBuilder()
    builder.add_character(Defeatist)
    stat = builder.build(base)
    assert stat.py_atk == 20
    assert stat.sp_atk == 30
    base.hp.lose(50)
    builder.add_character(Defeatist)
    stat = builder.build(base)
    assert stat.py_atk == 10
    assert stat.sp_atk == 15


# ごちゃごちゃしてる
def test_plus_and_minus():
    a = Monster()
    a.character = Plus
    b = Monster()
    b.character = Minus
    base = Monster(sp_atk=50)
    builder = StatBuilder()
    builder.add_monster(a)
    stat = builder.build(base)
    assert stat.sp_atk == 50
    builder.add_partner(b)
    stat = builder.build(base)
    assert stat.sp_atk == 75


def test_thick_club():
    other = Monster()
    cubone = Monster()
    cubone.name = 'Cubone'
    cubone.item = ThickClub
    builder = StatBuilder()
    builder.add_monster(cubone)
    stat = builder.build(Monster(py_atk=50))
    assert stat.py_atk == 100
    builder.add_monster(other)
    stat = builder.build(Monster(py_atk=50))
    assert stat.py_atk == 50


def test_hp_gain_and_lose():
    hp = HitPoint(maximum=100)
    assert hp == 100
    hp.lose(50)
    assert hp == 50
    hp.lose(100)
    assert hp == 0
    hp.gain(150)
    assert hp == 100


def test_hp_full():
    hp = HitPoint(maximum=100)
    assert hp.full
    hp.lose(1)
    assert not hp.full
