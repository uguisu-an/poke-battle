import math
import enum
from typing import Set
from copy import deepcopy


class Sex(enum.IntEnum):
    Unknown = 0
    Male = 1
    Female = -1


class Type(enum.IntEnum):
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


class MoveStyle(enum.Enum):
    Other = 1
    Sound = 2
    Fang = 3
    Fist = 4


class Ability(enum.Enum):
    Nothing = 0
    Analyze = 1
    TintedLens = 2
    LiquidVoice = 3
    AirLock = 4
    Galvanize = 5
    LongReach = 6
    AuraBreak = 7
    ToughClaws = 8
    StrongJaw = 9
    Scrappy = 10
    Torrent = 11
    Guts = 12
    SolarPower = 13
    Overgrow = 14
    WaterBubble = 15
    SkySkin = 16
    # SkillLink = 17  連続技が5回になるのは個々のダメージに影響しない
    Reckless = 18
    SandForce = 19
    Infiltrator = 20
    Sniper = 21
    SlowStart = 22
    DarkAura = 23
    SheerForce = 24
    HugePower = 25
    Technician = 26
    Adaptability = 27
    CloudNine = 28
    FairyAura = 29
    Refridgerate = 30
    Aerilate = 31
    Pixilate = 32
    Normalize = 33
    IronFist = 34
    Blaze = 35
    Swarm = 36
    Hustle = 37
    Stakeout = 38
    Defeatist = 39
    Forecast = 40
    Unaware = 41
    Rivalry = 42


class Item(enum.Enum):
    Nothing = 0


mv_power = 120
mv_level = 50
# TODO: ノーマルスキン＋プラズマシャワー＋フライングプレスで複合タイプになることがある
# フライングプレスを格闘が加わる飛行技と考えれば、特製の処理で対処できそう
mv_type: Type = Type.Normal
mv_form: MoveForm = MoveForm.Physical
mv_style = MoveStyle.Other
mv_direct = False
# 自分の攻撃でダメージを負うかどうか
mv_reckless = False

at_stat = 100
at_rank = 0
at_type: Set[Type] = {}
at_sex = Sex.Unknown
at_item: Item = Item.Nothing
at_ability: Ability = Ability.Nothing

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
df_sex = Sex.Unknown
df_item: Item = Item.Nothing
df_ability: Ability = Ability.Nothing

# 補助技
df_with_reflect = False
df_with_light_screen = False
df_with_protect = False
df_with_water_sport = False
df_with_mud_sport = False
df_with_foresight = False
df_with_miracle_eye = False
df_with_magnet_rise = False
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
fairy_aura = False
dark_aura = False
aura_break = False

# TODO: Typeで直接取れるようにする
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


# 威力の計算
def _affected_power():
    mt = _affected_mv_type()
    bonus = 1.0
    bonus *= _terrain_bonus()
    if at_with_helping_hand:
        bonus *= 1.5
    if at_with_charge and mt == Type.Electric:
        bonus *= 2.0
    if at_with_battery and mv_form == MoveForm.Special:
        bonus *= 1.3
    if df_with_water_sport and mt == Type.Fire:
        bonus *= 1/3
    if df_with_mud_sport and mt == Type.Electric:
        bonus *= 1/3
    if at_ability == Ability.Analyze:
        bonus *= 1.3
    # スキン系は元々ノーマルだった技の威力を上げるのでここでは元のタイプを見る
    if at_ability in {Ability.Galvanize, Ability.Refridgerate,
                      Ability.Aerilate, Ability.Pixilate} and mv_type == Type.Normal:
        bonus *= 1.2
    if at_ability == Ability.Normalize:
        bonus *= 1.2
    if at_ability == Ability.ToughClaws and _mv_direct():
        bonus *= 1.3
    if at_ability == Ability.StrongJaw and mv_style == MoveStyle.Fang:
        bonus *= 1.5
    if at_ability == Ability.IronFist and mv_style == MoveStyle.Fist:
        bonus *= 1.2
    # HPが1/3以下のとき限定
    if at_ability == Ability.Torrent and _affected_mv_type() == Type.Water:
        bonus *= 1.5
    if at_ability == Ability.Overgrow and _affected_mv_type() == Type.Grass:
        bonus *= 1.5
    if at_ability == Ability.Blaze and _affected_mv_type() == Type.Fire:
        bonus *= 1.5
    if at_ability == Ability.Swarm and _affected_mv_type() == Type.Bug:
        bonus *= 1.5
    # ここまで
    if at_ability == Ability.WaterBubble and _affected_mv_type() == Type.Water:
        bonus *= 2.0
    if at_ability == Ability.Reckless and mv_reckless:
        bonus *= 1.2
    if at_ability == Ability.SandForce and _affected_weather() == Weather.Sandstorm and _affected_mv_type() in {Type.Rock, Type.Steel, Type.Ground}:
        bonus *= 1.3
    if at_ability == Ability.SheerForce:
        # 追加効果のある技限定
        # 代わりに追加効果が出なくなる
        bonus *= 1.3
    if at_ability == Ability.HugePower and mv_form == MoveForm.Physical:
        bonus *= 2.0
    if at_ability == Ability.Technician and mv_power <= 60:
        bonus *= 1.5
    if df_ability == Ability.WaterBubble and _affected_mv_type() == Type.Fire:
        bonus *= 0.5
    if at_ability == Ability.Rivalry and at_sex != Sex.Unknown:
        if at_sex == df_sex:
            bonus *= 1.25
        if at_sex + df_sex == 0:
            bonus *= 0.75
    if (_fairy_aura() and mt == Type.Fairy) or (_dark_aura() and mt == Type.Dark):
        if _aura_break():
            bonus *= 3/4
        else:
            bonus *= 4/3
    return mv_power * bonus


def _fairy_aura():
    return fairy_aura or (at_ability == Ability.FairyAura) or (df_ability == Ability.FairyAura)


def _dark_aura():
    return dark_aura or (at_ability == Ability.DarkAura) or (df_ability == Ability.DarkAura)


def _aura_break():
    return aura_break or (at_ability == Ability.AuraBreak) or (df_ability == Ability.AuraBreak)


# TODO: 浮遊に対応する
# 地形による補正
def _terrain_bonus():
    mt = _affected_mv_type()
    if Type.Flying not in _affected_at_type():
        if terrain == Terrain.Electric and mt == Type.Electric:
            return 1.5
        if terrain == Terrain.Mist and mt == Type.Dragon:
            return 0.5
        if terrain == Terrain.Grass and mt == Type.Grass:
            # TODO: Earthquake, Bulldoze, Magnitude * 0.5
            return 1.5
        if terrain == Terrain.Psychic and mt == Type.Psychic:
            return 1.5
    return 1.0


# 攻撃値と防御値の比
def _ratio():
    return _at_stat_with_rank() / _df_stat_with_rank()


def _affected_at_stat():
    bonus = 1.0
    # TODO: Droughtも対象？
    if at_with_flower_gift and _affected_weather() == Weather.Sunny:
        # 攻撃のみ
        bonus *= 1.5
    if at_ability == Ability.Guts:
        # 攻撃のみ
        # 状態異常時限定
        bonus *= 1.5
    # TODO: Droughtも対象？
    if at_ability == Ability.SolarPower and _affected_weather() == Weather.Sunny:
        # 特攻のみ
        bonus *= 1.5
    if at_ability == Ability.Hustle:
        # 攻撃のみ
        # 命中率が0.8倍になる
        bonus *= 1.5
    if at_ability == Ability.Defeatist:
        # 両方
        # 体力が半分以下のとき
        bonus *= 0.5
    if at_ability == Ability.SlowStart:
        # 攻撃のみ（素早さも）
        # 場に出てから５ターンの間
        bonus *= 0.5
    return at_stat * bonus


def _affected_df_stat():
    bonus = 1.0
    # TODO: Droughtも対象？
    if df_with_flower_gift and _affected_weather() == Weather.Sunny:
        # 特防のみ
        bonus *= 1.5
    return df_stat * bonus


# ランク補正のかかった攻撃値
def _at_stat_with_rank():
    if (df_ability == Ability.Unaware) or (critical_hit and at_rank < 0):
        return _affected_at_stat()
    return _stat_with_rank(_affected_at_stat(), at_rank)


# ランク補正のかかった防御値
def _df_stat_with_rank():
    if (at_ability == Ability.Unaware) or (critical_hit and df_rank > 0):
        return _affected_df_stat()
    return _stat_with_rank(_affected_df_stat(), df_rank)


def _stat_with_rank(stat, rank):
    return stat * _rank_bonus(rank)


# ランクによる補正
def _rank_bonus(rank):
    if rank > 0:
        return (rank + 2) / 2
    if rank < 0:
        return 2 / (-rank + 2)
    return 2 / 2


def _is_type_match():
    return _affected_mv_type() in _affected_at_type()


# タイプ一致による補正
def _type_match():
    if _is_type_match():
        if at_ability == Ability.Adaptability:
            return 2.0
        return 1.2
    return 1.0


def _affected_type_table():
    table = deepcopy(type_table)
    if gravity:
        # じゅうりょくはさかさバトルに先立つ
        table[Type.Ground][Type.Flying] = 1.0
    if df_with_foresight or at_ability == Ability.Scrappy:
        # TODO: さかさバトルの影響は？
        table[Type.Normal][Type.Ghost] = 1.0
        table[Type.Fighting][Type.Ghost] = 1.0
    if df_with_miracle_eye:
        # TODO: さかさバトルの影響は？
        table[Type.Psychic][Type.Dark] = 1.0
    if inverse_battle:
        return _inverse_type_table(table)
    return table


# さかさバトルの相性表に変更する
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


# 効果の影響を受けたわざタイプを得る
def _affected_mv_type():
    if at_with_electrify:
        return Type.Electric
    if ion_deluge and mv_type == Type.Normal:
        return Type.Electric
    if at_ability == Ability.LiquidVoice and mv_style == MoveStyle.Sound:
        return Type.Water
    if at_ability == Ability.Galvanize and mv_type == Type.Normal:
        return Type.Electric
    if at_ability == Ability.Refridgerate and mv_type == Type.Normal:
        return Type.Ice
    if at_ability == Ability.Pixilate and mv_type == Type.Normal:
        return Type.Fairy
    if at_ability == Ability.Aerilate and mv_type == Type.Normal:
        return Type.Flying
    if at_ability == Ability.Normalize:
        if ion_deluge:
            return Type.Electric
        return Type.Normal
    return mv_type


def _affected_at_type():
    at = set(at_type.copy())
    if at_ability == Ability.Forecast:
        if weather in {Weather.Sunny, Weather.Drought}:
            at = {Type.Fire}
        if weather in {Weather.Rainy, Weather.HeavyRainy}:
            at = {Type.Water}
        if weather in {Weather.Hailstorm}:
            at = {Type.Ice}
    if at_with_trick_or_treat:
        at.add(Type.Ghost)
    if at_with_forests_curse:
        at.add(Type.Grass)
    return at


def _affected_df_type():
    dt = set(df_type.copy())
    if df_with_trick_or_treat:
        dt.add(Type.Ghost)
    if df_with_forests_curse:
        dt.add(Type.Grass)
    return dt


def _type_effect():
    tt = _affected_type_table()
    mt = _affected_mv_type()
    dt = _affected_df_type()
    if df_with_magnet_rise and not gravity and mt == Type.Ground:
        return 0
    e = 1.0
    for t in dt:
        if t is None:
            continue
        e *= tt[mt][t]
    return e


def _critical_bonus():
    if critical_hit:
        if at_ability == Ability.Sniper:
            return 1.5 * 1.5
        return 1.5
    return 1.0


def _affected_weather():
    if at_ability in {Ability.AirLock, Ability.CloudNine}:
        return Weather.Calm
    return weather


def _weather_effect():
    mt = _affected_mv_type()
    wr = _affected_weather()
    # TODO: WeatherBallに対応する
    # TODO: SolarBeamに対応する
    if wr == Weather.Sunny:
        if mt == Type.Water:
            return 0.5
        if mt == Type.Fire:
            return 1.5
    if wr == Weather.Rainy:
        if mt == Type.Fire:
            return 0.5
        if mt == Type.Water:
            return 1.5
    if wr == Weather.Drought:
        if mt == Type.Water:
            return 0
        if mt == Type.Fire:
            return 1.5
    if wr == Weather.HeavyRainy:
        if mt == Type.Fire:
            return 0
        if mt == Type.Water:
            return 1.5
    return 1.0


def _other_bonus():
    bonus = 1.0
    # 先制した時だけ、相手の攻撃技で
    if at_with_me_first:
        bonus *= 1.5
    if at_with_burn and mv_form == MoveForm.Physical:
        bonus *= 0.5
    if df_with_light_screen and mv_form == MoveForm.Special and at_ability != Ability.Infiltrator:
        bonus *= 0.5
    if df_with_reflect and mv_form == MoveForm.Physical and at_ability != Ability.Infiltrator:
        bonus *= 0.5
    if df_with_protect:
        bonus *= 0
    if df_with_friend_guard:
        bonus *= 0.75
    if at_ability == Ability.TintedLens and _type_effect() < 1:
        bonus *= 2.0
    return bonus


def _mv_direct():
    if at_ability == Ability.LongReach:
        return False
    return mv_direct


# TODO: ワンダールームはこの計算機の外、Monsterを生成する段階で作用する
