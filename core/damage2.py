import math
import enum
from typing import Set
from copy import deepcopy


class Type(enum.Enum):
    Normal = 0
    Fire = 1
    Water = 2
    Electric = 3
    Grass = 4
    Ice = 5
    Fighting = 6
    Poison = 7
    Ground = 8
    Flying = 9
    Psychic = 10
    Bug = 11
    Rock = 12
    Ghost = 13
    Dragon = 14
    Dark = 15
    Steel = 16
    Fairy = 17


class MoveForm(enum.Enum):
    Physical = 0
    Special = 1


class Weather(enum.Enum):
    Calm = 0
    Sunny = 1
    Rainy = 2
    Drought = 3
    HeavyRainy = 4
    Hailstorm = 5
    Sandstorm = 6
    Turbulence = 7


class Terrain(enum.Enum):
    Common = 0
    Electric = 1
    Grass = 2
    Mist = 3
    Psychic = 4


mv_power = 120
mv_level = 50
# TODO: ノーマルスキン＋プラズマシャワー＋フライングプレスで複合タイプになることがある
mv_type: Type = Type.Normal
mv_form: MoveForm = MoveForm.Physical

at_stat = 100
at_rank = 0
at_type: Set[Type] = {}
at_item = None
at_ability = None

# 補助技
at_with_helping_hand = False
at_with_me_first = False
at_with_electrify = False
at_with_charge = False
at_with_trick_or_treat = False
at_with_forests_curse = False
# 状態異常
at_with_burn = False
# 味方の特性
at_with_battery = False
at_with_flower_gift = False

df_stat = 100
df_rank = 0
df_type: Set[Type] = {}
df_item = None
df_ability = None

# 補助技
df_with_reflect = False
df_with_light_screen = False
df_with_protect = False
df_with_water_sport = False
df_with_mud_sport = False
df_with_foresight = False
df_with_miracle_eye = False
df_with_magnet_rise = False
df_with_substitute = False
df_with_trick_or_treat = False
df_with_forests_curse = False
# 味方の特性
df_with_flower_gift = False
df_with_friend_guard = False

critical_hit = False
weather: Weather = Weather.Calm
terrain: Terrain = Terrain.Common

gravity = False
ion_deluge = False
inverse_battle = False

type_table = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 0],
    [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1],
    [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1],
    [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1],
    [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1],
    [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1],
    [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 1],
    [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2],
    [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1],
    [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1],
    [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5],
    [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0],
    [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5],
    [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2],
    [1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1],
]


def calc():
    damage = _base_damage()
    damage *= _type_match()
    damage *= _type_effect()
    damage *= _weather_effect()
    damage *= _critical_bonus()
    damage *= _other_bonus()
    return math.floor(damage)


def _base_damage():
    return _affected_power() * (mv_level+5) * _ratio() / 125 + 2


def _affected_power():
    bonus = 1.0
    bonus *= _terrain_bonus()
    if at_with_helping_hand:
        bonus *= 1.5
    if at_with_charge and mv_type == Type.Electric:
        bonus *= 2.0
    if at_with_battery and mv_form == MoveForm.Special:
        bonus *= 1.3
    return mv_power * bonus


# TODO: 浮遊に対応する
def _terrain_bonus():
    if Type.Flying not in at_type:
        if terrain == Terrain.Electric and mv_type == Type.Electric:
            return 1.5
        if terrain == Terrain.Mist and mv_type == Type.Dragon:
            return 0.5
        if terrain == Terrain.Grass and mv_type == Type.Grass:
            # TODO: Earthquake, Bulldoze, Magnitude * 0.5
            return 1.5
        if terrain == Terrain.Psychic and mv_type == Type.Psychic:
            return 1.5
    return 1.0


def _ratio():
    return _at_stat_with_rank() / _df_stat_with_rank()


def _at_stat_with_rank():
    if critical_hit and at_rank < 0:
        return at_stat
    return _stat_with_rank(at_stat, at_rank)


def _df_stat_with_rank():
    if critical_hit and df_rank > 0:
        return df_stat
    return _stat_with_rank(df_stat, df_rank)


def _stat_with_rank(stat, rank):
    return stat * _rank_bonus(rank)


def _rank_bonus(rank):
    if rank > 0:
        return (rank + 2) / 2
    if rank < 0:
        return 2 / (-rank + 2)
    return 2 / 2


def _is_type_match():
    return mv_type in at_type


def _type_match():
    if _is_type_match():
        return 1.2
    return 1.0


def _affected_type_table():
    table = deepcopy(type_table)
    if gravity:
        table[Type.Ground.value][Type.Flying.value] = 1.0
    if inverse_battle:
        return _inverse_type_table(table)
    return table


def _inverse_type_table(type_table_copy):
    return list(map(_inverse_type_table_row, type_table_copy))


def _inverse_type_table_row(row):
    return list(map(_inverse_type_table_cell, row))


def _inverse_type_table_cell(type_effect):
    if type_effect > 1:
        return 0.5
    if type_effect < 1:
        return 2.0
    return 1.0


def _affected_move_type():
    if ion_deluge and mv_type == Type.Normal:
        return Type.Electric
    return mv_type


def _type_effect():
    tt = _affected_type_table()
    mt = _affected_move_type()
    e = 1.0
    for t in df_type:
        if t is None:
            continue
        e *= tt[mt.value][t.value]
    return e


def _critical_bonus():
    if critical_hit:
        return 1.5
    return 1.0


def _weather_effect():
    # TODO: WeatherBallに対応する
    # TODO: SolarBeamに対応する
    if weather == Weather.Sunny:
        if mv_type == Type.Water:
            return 0.5
        if mv_type == Type.Fire:
            return 1.5
    if weather == Weather.Rainy:
        if mv_type == Type.Fire:
            return 0.5
        if mv_type == Type.Water:
            return 1.5
    if weather == Weather.Drought:
        if mv_type == Type.Water:
            return 0
        if mv_type == Type.Fire:
            return 1.5
    if weather == Weather.HeavyRainy:
        if mv_type == Type.Fire:
            return 0
        if mv_type == Type.Water:
            return 1.5
    return 1.0


def _other_bonus():
    bonus = 1.0
    # 先制した時だけ、相手の攻撃技で
    if at_with_me_first:
        bonus *= 1.5
    if at_with_burn and mv_form == MoveForm.Physical:
        bonus *= 0.5
    return bonus


# TODO: ワンダールームはこの計算機の外、Monsterを生成する段階で作用する
