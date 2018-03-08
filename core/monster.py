from core.type import Normal
from core.level import Level


class Monster:
    type = Normal
    level = Level(1)

    def __init__(self, py_atk=1, sp_atk=1, py_def=1, sp_def=1):
        self.py_atk = py_atk
        self.sp_atk = sp_atk
        self.py_def = py_def
        self.sp_def = sp_def

    # ダメージ計算用の攻撃値を求める
    def attack(self, move):
        return move.select_attack(self) * self.level.get_rate()

    # ダメージ計算用の防御値を求める
    def defend(self, move):
        return move.select_defence(self) * 50


class MonsterStat:
    def __init__(self, hp=0, max_hp=0, py_atk=0, sp_atk=0, py_def=0, sp_def=0):
        self.hp = hp
        self.max_hp = max_hp
        self.py_atk = py_atk
        self.sp_atk = sp_atk
        self.py_def = py_def
        self.sp_def = sp_def
