from core.type import Grass
from core.move import SpecialAttack
from core.effect.weather import *


def new_solar_ball(weather):
    if weather in (Rainy, HeavyRainy, Hailstorm, Sandstorm):
        return WeakSolarBeam()
    return SolarBeam()


class SolarBeam(SpecialAttack):
    name = 'Solar Beam'
    type = Grass
    power = 120


class WeakSolarBeam(SpecialAttack):
    name = 'Solar Beam'
    type = Grass
    power = 60
