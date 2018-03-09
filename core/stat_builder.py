from copy import copy
from core.character import *
from core.item import *
from core.effect.weather import *
from core.monster import Monster


class StatBuilder:
    _monster = None
    _monster_name = None
    _monster_character = None
    _item = None
    _partner = None
    _partner_character = None
    _weather = None

    def add_character(self, character):
        self._monster_character = character

    def add_item(self, item):
        self._item = item

    def add_weather(self, weather):
        self._weather = weather

    def add_monster(self, monster):
        self._monster = monster
        self._monster_name = monster.name
        self.add_character(monster.character)
        self.add_item(monster.item)

    def add_partner(self, partner):
        self._partner = partner
        self._partner_character = partner.character

    def build(self, base: Monster) -> Monster:
        stat = copy(base)
        if self._monster_character == Defeatist and base.hp.current * 2 <= base.hp.maximum:
            stat.py_atk *= 0.5
            stat.sp_atk *= 0.5
        if self._monster_character == Plus and self._partner_character == Minus:
            stat.sp_atk *= 1.5
        if self._monster_character == Minus and self._partner_character == Plus:
            stat.sp_atk *= 1.5
        if self._item == ThickClub and self._monster_name in ('Cubone', 'Marowak'):
            stat.py_atk *= 2.0
        if self._monster_character == FlowerGift and self._weather == Sunny:
            stat.py_atk *= 1.5
        return stat
