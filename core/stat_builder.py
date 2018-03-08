from copy import copy
from core.monster import MonsterStat
from core.character import *


class StatBuilder:
    _character = None
    _item = None

    def add_character(self, character):
        self._character = character

    def add_item(self, item):
        self._item = item

    def build(self, base: MonsterStat) -> MonsterStat:
        stat = copy(base)
        if self._character == Defeatist and base.hp * 2 <= base.max_hp:
            stat.py_atk *= 0.5
            stat.sp_atk *= 0.5
        return stat
