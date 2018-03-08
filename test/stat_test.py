from core.stat import *
from core.level import *


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
