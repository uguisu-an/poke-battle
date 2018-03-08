from core.move.solarbeam import *
from core.move.weatherball import *


class MoveFactory:
    def __init__(self, environment):
        self.environment = environment

    def create(self, name):
        if name == WeatherBall.name:
            return new_weather_ball(self.environment.weather)
        if name == SolarBeam.name:
            return new_solar_ball(self.environment.weather)
        return None
