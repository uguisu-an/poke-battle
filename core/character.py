from collections import namedtuple
from core.effect.weather import Sunny


Character = namedtuple('Character', 'name')
Defeatist = Character('Defeatist')
Plus = Character('Plus')
Minus = Character('Minus')
FlowerGift = Character('Flower Gift')
BrainForce = Character('Brain Force')
TintedLens = Character('Tinted Lens')
Sniper = Character('Sniper')
HardRock = Character('HardRock')
Filter = Character('Filter')
Multiscale = Character('Multiscale')
PhantomGuard = Character('PhantomGuard')


class EventListener:
    def listen(self, sender):
        pass


class ObservableFlowerGift(EventListener):
    name = 'Flower Gift'

    @staticmethod
    def enforce(monster):
        monster.py_atk *= 1.5
        monster.sp_def *= 1.5

    def __init__(self, owner):
        self.owner = owner
        self.active = False

    def listen(self, sender):
        sender.on('field_initialized', self.on_field_initialized)
        sender.on('weather_changed', self.on_weather_changed)

    def on_field_initialized(self, field):
        if not self.active:
            return
        for team in field.teams:
            if not any(m == self.owner for m in team.monsters):
                continue
            map(self.enforce, team.monsters)

    def on_weather_changed(self, weather):
        self.active = (weather == Sunny)


class ObservableHardRock(EventListener):
    name = 'Hard Rock'

    @staticmethod
    def affect(damage):
        damage *= 0.75

    def __init__(self, owner):
        self.owner = owner

    def listen(self, sender):
        sender.on('super_effective', self.on_super_effective)

    def on_super_effective(self, attacker, defender, damage):
        if defender == self.owner:
            self.affect(damage)


class ObservablePhantomGuard(EventListener):
    name = 'Phantom Guard'

    @staticmethod
    def affect(damage):
        damage *= 0.5

    def __init__(self, owner):
        self.owner = owner

    def listen(self, sender):
        sender.on('damage_defender', self.on_damage_defender)

    def on_damage_defender(self, attacker, defender, damage):
        if defender == self.owner and defender.hp == defender.max_hp:
            self.affect(damage)
