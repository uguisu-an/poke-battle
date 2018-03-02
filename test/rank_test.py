from core.rank import Rank


def test_rank_ratio():
    assert Rank(0).ratio() == 2/2
    assert Rank(6).ratio() == 8/2
    assert Rank(-6).ratio() == 2/8


def test_rank_up_limit():
    rank = Rank(6)
    rank.up()
    assert rank.ratio() == 8/2


def test_rank_down_limit():
    rank = Rank(-6)
    rank.down()
    assert rank.ratio() == 2/8
