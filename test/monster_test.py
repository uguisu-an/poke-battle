from core.move import *
from core.monster import *
from core.level import *


def test_attacking_monster():
    monster = Monster(py_atk=2, sp_atk=3)
    monster.level = Level(50)
    assert monster.attack(PhysicalAttack) == 44
    assert monster.attack(SpecialAttack) == 66


def test_defending_monster():
    monster = Monster(py_def=3, sp_def=2)
    monster.level = Level(50)
    assert monster.defend(PhysicalAttack) == 150
    assert monster.defend(SpecialAttack) == 100
