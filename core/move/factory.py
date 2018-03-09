from core.move.solarbeam import *
from core.move.weatherball import *
from core.type import InverseType
from core.effect import *


class MoveFactory:
    def __init__(self, environment):
        self.environment = environment

    def create(self, name):
        if name == WeatherBall.name:
            return new_weather_ball(self.environment.weather)
        if name == SolarBeam.name:
            return new_solar_ball(self.environment.weather)
        return None


class MoveBuilder:
    def __init__(self):
        self.inverse = False

    def add_effect(self, effect):
        if effect == InverseBattle:
            self.inverse = True

    def build(self, move):
        if self.inverse:
            move.type = InverseType(move.type)
        return move
