import math
import enum
from typing import Set


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


class Weather(enum.Enum):
    Calm = 0
    Sunny = 1
    Rainy = 2
    Drought = 3
    HeavyRainy = 4
    Hailstorm = 5
    Sandstorm = 6
    Turbulence = 7


mv_power = 120
mv_level = 50
mv_type: Type = Type.Normal

at_stat = 100
at_rank = 0
at_type: Set[Type] = {}
at_item = None
at_ability = None

df_stat = 100
df_rank = 0
df_type: Set[Type] = {}
df_item = None
df_ability = None

critical_hit = False
weather: Weather = Weather.Calm
field = {}
other_effect = {}

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
    return math.floor(damage)


def _base_damage():
    return mv_power * (mv_level+5) * _ratio() / 125 + 2


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


def _type_effect():
    e = 1.0
    for t in df_type:
        if t is None:
            continue
        e *= type_table[mv_type.value][t.value]
    return e


def _critical_bonus():
    if critical_hit:
        return 1.5
    return 1.0


def _weather_effect():
    # TODO: WeatherBallに対応する
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
