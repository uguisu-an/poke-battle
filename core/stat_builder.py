from copy import copy
from core.monster import MonsterStat
from core.character import *


class StatBuilder:
    _monster = None
    _monster_character = None
    _item = None
    _partner = None
    _partner_character = None

    def add_character(self, character):
        self._monster_character = character

    def add_item(self, item):
        self._item = item

    def add_monster(self, monster):
        self._monster = monster
        self._monster_character = monster.character
        self._item = monster.item

    def add_partner(self, partner):
        self._partner = partner
        self._partner_character = partner.character

    def build(self, base: MonsterStat) -> MonsterStat:
        stat = copy(base)
        if self._monster_character == Defeatist and base.hp * 2 <= base.max_hp:
            stat.py_atk *= 0.5
            stat.sp_atk *= 0.5
        if self._monster_character == Plus and self._partner_character == Minus:
            stat.sp_atk *= 1.5
        if self._monster_character == Minus and self._partner_character == Plus:
            stat.sp_atk *= 1.5
        return stat
