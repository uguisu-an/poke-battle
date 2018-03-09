import core.type as t
from core.move import *
from core.level import Level
from core.damage import *
from core.event import *


def test_base_damage():
    assert base_damage(120, 1.0) == 122
    assert base_damage(120, 2.0) == 242


def test_type_match():
    move = Attack()
    move.type = t.Normal
    assert move.type_match(t.Normal)
    assert not move.type_match(t.Dragon)


def test_type_match_up():
    move = Attack()
    move.type = t.Ground
    assert move.type_match_up(t.Fire, t.Flying) == 0
    assert move.type_match_up(t.Fire, t.Grass) == 1.0
    assert move.type_match_up(t.Fire, t.Electric) == 4.0


def test_randomized_damage():
    assert randomized(100, randomizer=minimizer) == 85
    assert randomized(100, randomizer=maximizer) == 100


def test_damage_calculator():
    move = PhysicalAttack()
    move.type = t.Normal
    move.power = 120
    attacker = Monster(py_atk=200, level=50)
    defender = Monster(py_def=150)
    damage = DamageCalculator(move, attacker, defender)
    damage.add_randomizer(maximizer)
    assert damage.calc() == 86


def test_phantom_guard():
    event = EventEmitter()
    owner = Monster(hp=50, max_hp=50)
    guard = ObservablePhantomGuard(owner)
    guard.listen(event)
    damage = Damage(100)
    event.emit(DamageDefender, None, owner, damage)
    assert damage == 50
