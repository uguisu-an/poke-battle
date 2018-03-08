from core.type import Grass
from core.move import SpecialAttack
from core.effect.weather import *


def _stat_depends_on_weather(weather):
    if weather in (Rainy, HeavyRainy, Hailstorm, Sandstorm):
        return 60
    return 120


class SolarBeam(SpecialAttack):
    name = 'Solar Beam'
    type = Grass
    power = 120

    def affected_by(self, weather):
        self.power = _stat_depends_on_weather(weather)
