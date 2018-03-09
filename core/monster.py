from core.type import Normal
from core.level import Level
from core.stat import *


class Monster:
    name = ''
    type = Normal
    level = Level(1)
    item = None
    character = None

    def __init__(self, level=1, hp=0, py_atk=1, sp_atk=1, py_def=1, sp_def=1):
        # TODO: Factoryで初期化する
        self.level = Level(level)
        self.hp = HitPoint(maximum=hp)
        self.py_atk = py_atk
        self.sp_atk = sp_atk
        self.py_def = py_def
        self.sp_def = sp_def

    # TODO: ここから下は切り出した方がいいかも

    # ダメージ計算用の攻撃値を求める
    def attack(self, move):
        return move.select_attack(self) * self.level.get_rate()

    # ダメージ計算用の防御値を求める
    def defend(self, move):
        return move.select_defence(self) * 50
