from core.move import SpecialAttack
from core.type import Normal, Fire, Water, Ice, Rock
from core.effect.weather import *


def new_weather_ball(weather):
    if weather in (Sunny, Drought):
        return FireWeatherBall()
    if weather in (Rainy, HeavyRainy):
        return WaterWeatherBall()
    if weather in (Hailstorm,):
        return IceWeatherBall()
    if weather in (Sandstorm,):
        return RockWeatherBall()
    return WeatherBall()


class WeatherBall(SpecialAttack):
    name = 'Weather Ball'
    type = Normal
    power = 50


class FireWeatherBall(SpecialAttack):
    name = 'Weather Ball'
    type = Fire
    power = 100


class WaterWeatherBall(SpecialAttack):
    name = 'Weather Ball'
    type = Water
    power = 100


class IceWeatherBall(SpecialAttack):
    name = 'Weather Ball'
    type = Ice
    power = 100


class RockWeatherBall(SpecialAttack):
    name = 'Weather Ball'
    type = Rock
    power = 100
