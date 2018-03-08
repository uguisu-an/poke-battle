import core.type as t
from core.move import SpecialAttack
from core.effect.weather import *


def _stat_depends_on_weather(weather):
    if weather in (Sunny, Drought):
        return 100, t.Fire
    if weather in (Rainy, HeavyRainy):
        return 100, t.Water
    if weather in (Hailstorm,):
        return 100, t.Ice
    if weather in (Sandstorm,):
        return 100, t.Rock
    return 50, t.Normal


class WeatherBall(SpecialAttack):
    name = 'Weather Ball'
    type = t.Normal
    power = 50

    def affected_by(self, weather):
        self.power, self.type = _stat_depends_on_weather(weather)
