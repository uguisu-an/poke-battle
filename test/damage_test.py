from importlib import reload
import core.damage2 as d2


SUPER_EFFECT_2 = 109
SUPER_EFFECT_4 = 219


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


def test_weather_effect():
    d2.weather = d2.Weather.Sunny
    d2.mv_type = d2.Type.Water
    assert d2.calc() == 27
    d2.mv_type = d2.Type.Fire
    assert d2.calc() == 82


def test_rank_bonus():
    d2.at_rank = 1
    d2.df_rank = -2
    assert d2.calc() == 160


def test_critical_effect():
    d2.critical_hit = True
    d2.at_rank = -1
    d2.df_rank = 1
    assert d2.calc() == 82
    d2.at_rank = 1
    assert d2.calc() == 121
    d2.df_rank = -2
    assert d2.calc() == 240


def test_gravity():
    d2.mv_type = d2.Type.Ground
    d2.df_type = {d2.Type.Flying}
    assert d2.calc() == 0
    d2.gravity = True
    assert d2.calc() == 54
    d2.gravity = False
    assert d2.calc() == 0


def test_electric_terrain():
    d2.mv_type = d2.Type.Electric
    d2.terrain = d2.Terrain.Electric
    assert d2.calc() == 81
    d2.at_type = {d2.Type.Flying}
    assert d2.calc() == 54


def test_ion_deluge():
    d2.ion_deluge = True
    d2.mv_type = d2.Type.Normal
    d2.df_type = {d2.Type.Ground}
    assert d2.calc() == 0
    d2.df_type = {d2.Type.Water, d2.Type.Flying}
    assert d2.calc() == 219


def test_inverse_battle():
    d2.inverse_battle = True
    d2.mv_type = d2.Type.Ground
    d2.df_type = {d2.Type.Flying}
    assert d2.calc() == SUPER_EFFECT_2
    # 重力と複合した場合は地面：飛行が等倍になる（重力が先に反映される）
    d2.gravity = True
    assert d2.calc() == 54

