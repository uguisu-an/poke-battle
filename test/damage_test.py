from importlib import reload
import core.damage2 as d2


STANDARD = 54
SUPER_EFFECT_2 = 109
SUPER_EFFECT_2_AND_MATCH = 130
SUPER_EFFECT_4 = 219


def setup():
    reload(d2)


def test_default_setup():
    assert d2.calc() == STANDARD


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
    assert d2.calc() == STANDARD
    d2.gravity = False
    assert d2.calc() == 0


def test_electric_terrain():
    d2.mv_type = d2.Type.Electric
    d2.terrain = d2.Terrain.Electric
    assert d2.calc() == 81
    d2.at_type = {d2.Type.Flying}
    assert d2.calc() == STANDARD
    d2.gravity = True
    assert d2.calc() == 81


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
    assert d2.calc() == STANDARD


def test_helping_hand():
    d2.at_with_helping_hand = True
    assert d2.calc() == 81


def test_charge():
    d2.at_with_electrify = True
    d2.at_with_charge = True
    assert d2.calc() == 107


def test_battery():
    d2.at_with_battery = True
    d2.mv_form = d2.MoveForm.Physical
    assert d2.calc() == 54
    d2.mv_form = d2.MoveForm.Special
    assert d2.calc() == 70


def test_me_first():
    d2.at_with_me_first = True
    assert d2.calc() == 82


def test_burn():
    d2.at_with_burn = True
    d2.mv_form = d2.MoveForm.Physical
    assert d2.calc() == 27
    d2.mv_form = d2.MoveForm.Special
    assert d2.calc() == 54


def test_trick_or_treat():
    d2.mv_type = d2.Type.Ghost
    d2.at_with_trick_or_treat = True
    assert d2.calc() == 65
    d2.df_with_trick_or_treat = True
    assert d2.calc() == 131


def test_forests_curse():
    d2.mv_type = d2.Type.Grass
    d2.at_with_forests_curse = True
    assert d2.calc() == 65
    d2.df_with_forests_curse = True
    assert d2.calc() == 32


def test_flower_gift():
    # d2.at_with_flower_gift = True
    d2.at_ability = d2.Ability.FlowerGift
    d2.weather = d2.Weather.Drought
    d2.mv_form = d2.MoveForm.Physical
    assert d2.calc() == 81
    # 本来は特防に補正がかかるので物理技に対して効果がない
    d2.df_with_flower_gift = True
    assert d2.calc() == 54


def test_reflect():
    d2.df_with_reflect = True
    d2.mv_form = d2.MoveForm.Physical
    assert d2.calc() == 27
    d2.mv_form = d2.MoveForm.Special
    assert d2.calc() == 54


def test_light_screen():
    d2.df_with_light_screen = True
    d2.mv_form = d2.MoveForm.Physical
    assert d2.calc() == 54
    d2.mv_form = d2.MoveForm.Special
    assert d2.calc() == 27


def test_foresight():
    d2.mv_type = d2.Type.Fighting
    d2.df_type = {d2.Type.Ghost}
    assert d2.calc() == 0
    d2.df_with_foresight = True
    assert d2.calc() == 54


def test_magnet_rise():
    d2.df_with_magnet_rise = True
    d2.mv_type = d2.Type.Ground
    assert d2.calc() == 0
    d2.gravity = True
    assert d2.calc() == 54


def test_miracle_eye():
    d2.df_with_miracle_eye = True
    d2.mv_type = d2.Type.Psychic
    d2.df_type = {d2.Type.Dark}
    assert d2.calc() == 54


def test_water_sport():
    d2.df_with_water_sport = True
    assert d2.calc() == 54
    d2.mv_type = d2.Type.Fire
    assert d2.calc() == 19


def test_analyze():
    # TODO: 最後に攻撃したとき限定
    d2.at_ability = d2.Ability.Analyze
    assert d2.calc() == 70


def test_not_effective():
    d2.mv_type = d2.Type.Dark
    d2.df_type = {d2.Type.Fighting, d2.Type.Dark}
    assert d2.calc() == 13
    d2.at_ability = d2.Ability.TintedLens
    assert d2.calc() == 27


def test_liquid_voice():
    d2.at_ability = d2.Ability.LiquidVoice
    d2.df_type = {d2.Type.Fire}
    assert d2.calc() == 54
    d2.mv_style = d2.MoveStyle.Sound
    assert d2.calc() == SUPER_EFFECT_2


def test_air_lock():
    d2.at_ability = d2.Ability.AirLock
    d2.mv_type = d2.Type.Water
    d2.weather = d2.Weather.Drought
    assert d2.calc() == 54


def test_aura_break():
    d2.fairy_aura = True
    d2.mv_type = d2.Type.Fairy
    assert d2.calc() == 72
    d2.at_ability = d2.Ability.AuraBreak
    assert d2.calc() == 41


def test_galvanize():
    d2.at_ability = d2.Ability.Galvanize
    d2.mv_type = d2.Type.Normal
    d2.df_type = {d2.Type.Water}
    assert d2.calc() == 130


def test_normalize_and_ion_deluge():
    d2.at_ability = d2.Ability.Normalize
    d2.ion_deluge = True
    d2.mv_type = d2.Type.Water
    d2.df_type = {d2.Type.Water}
    # プラズマシャワーが適用される
    assert d2.calc() == 130


def test_tough_claws():
    d2.at_ability = d2.Ability.ToughClaws
    d2.mv_direct = True
    assert d2.calc() == 70


def test_strong_jaw():
    d2.at_ability = d2.Ability.StrongJaw
    d2.mv_style = d2.MoveStyle.Fang
    assert d2.calc() == 81


def test_solar_power():
    d2.at_ability = d2.Ability.SolarPower
    assert d2.calc() == 54
    d2.weather = d2.Weather.Sunny
    assert d2.calc() == 81


def test_water_bubble_for_attacker():
    d2.at_ability = d2.Ability.WaterBubble
    d2.mv_type = d2.Type.Water
    assert d2.calc() == 107


def test_water_bubble_for_defender():
    d2.mv_type = d2.Type.Fire
    d2.df_ability = d2.Ability.WaterBubble
    assert d2.calc() == 28


def test_reckless():
    d2.at_ability = d2.Ability.Reckless
    d2.mv_reckless = True
    assert d2.calc() == 65


def test_sand_force():
    d2.at_ability = d2.Ability.SandForce
    d2.mv_type = d2.Type.Rock
    d2.weather = d2.Weather.Sandstorm
    assert d2.calc() == 70


def test_infiltrator():
    d2.at_ability = d2.Ability.Infiltrator
    d2.df_with_reflect = True
    d2.df_with_light_screen = True
    assert d2.calc() == STANDARD


def test_sniper():
    d2.at_ability = d2.Ability.Sniper
    d2.critical_hit = True
    assert d2.calc() == 123


def test_technician():
    d2.at_ability = d2.Ability.Technician
    d2.mv_power = 60
    assert d2.calc() == 41
    d2.mv_power = 70
    assert d2.calc() == 32
    d2.mv_power = 90
    assert d2.calc() == 41


def test_adaptability():
    d2.at_ability = d2.Ability.Adaptability
    d2.at_type = {d2.Type.Normal}
    d2.mv_type = d2.Type.Normal
    assert d2.calc() == 109


def test_forecast():
    d2.at_ability = d2.Ability.Forecast
    d2.weather = d2.Weather.Sunny
    d2.mv_type = d2.Type.Fire
    assert d2.calc() == 98
    d2.weather = d2.Weather.Calm
    assert d2.calc() == 54


def test_unaware_for_attacker():
    d2.at_ability = d2.Ability.Unaware
    d2.df_rank = 6
    assert d2.calc() == 54
    d2.at_rank = 2
    assert d2.calc() == 107


def test_unaware_for_defender():
    d2.df_ability = d2.Ability.Unaware
    d2.at_rank = 6
    assert d2.calc() == 54
    d2.df_rank = 2
    assert d2.calc() == 28


def test_rivalry():
    d2.at_ability = d2.Ability.Rivalry
    assert d2.calc() == 54
    d2.at_sex = d2.Sex.Male
    d2.df_sex = d2.Sex.Male
    assert d2.calc() == 68
    d2.df_sex = d2.Sex.Female
    assert d2.calc() == 41


def test_brain_force():
    d2.at_ability = d2.Ability.BrainForce
    d2.mv_type = d2.Type.Bug
    d2.df_type = {d2.Type.Grass}
    assert d2.calc() == 131


def test_plus_minus():
    d2.at_ability = d2.Ability.Plus
    d2.at_with_minus = True
    assert d2.calc() == 81
    d2.df_ability = d2.Ability.Minus
    d2.df_with_plus = True
    assert d2.calc() == 54


def test_levitate():
    d2.at_ability = d2.Ability.Levitate
    d2.mv_type = d2.Type.Electric
    d2.terrain = d2.Terrain.Electric
    assert d2.calc() == STANDARD
    d2.gravity = True
    assert d2.calc() == 81


def test_levitate_for_defender():
    d2.df_ability = d2.Ability.Levitate
    d2.mv_type = d2.Type.Ground
    assert d2.calc() == 0
    d2.gravity = True
    assert d2.calc() == STANDARD


def test_protean():
    d2.at_ability = d2.Ability.Protean
    d2.mv_type = d2.Type.Fire
    assert d2.calc() == 65
    d2.mv_type = d2.Type.Water
    assert d2.calc() == 65
    d2.mv_type = d2.Type.Bug
    assert d2.calc() == 65


def test_yoga_power():
    d2.at_ability = d2.Ability.YogaPower
    d2.mv_form = d2.MoveForm.Physical
    assert d2.calc() == 107
