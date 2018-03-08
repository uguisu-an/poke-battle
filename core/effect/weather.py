from collections import namedtuple
import core.type as t


def adjust(weather, move):
    if weather == 'Sunny':
        sunny_adjust(move)
    if weather == 'Drought':
        drought_adjust(move)
    if weather == 'Rain':
        rainy_adjust(move)
    if weather == 'Heavy Rain':
        heavy_rainy_adjust(move)
    if weather == 'Hail':
        hailstorm_adjust(move)
    if weather == 'Sandstorm':
        sandstorm_adjust(move)


def sunny_adjust(move):
    if move.type == t.Fire:
        move.power *= 1.5
    if move.type == t.Water:
        move.power *= 0.5


def drought_adjust(move):
    sunny_adjust(move)
    if move.type == t.Water:
        move.power = 0


def rainy_adjust(move):
    if move.type == t.Fire:
        move.power *= 0.5
    if move.type == t.Water:
        move.power *= 1.5
    if move.name == 'Solar Beam':
        move.power *= 0.5


def heavy_rainy_adjust(move):
    rainy_adjust(move)
    if move.type == t.Fire:
        move.power = 0


def hailstorm_adjust(move):
    if move.name == 'Solar Beam':
        move.power *= 0.5


def sandstorm_adjust(move):
    if move.name == 'Solar Beam':
        move.power *= 0.5


Weather = namedtuple('Weather', 'name')
NoWeather = Weather('NoWeather')
Sunny = Weather('Sunny')
Rainy = Weather('Rainy')
Drought = Weather('Drought')
HeavyRainy = Weather('Heavy Rainy')
Turbulence = Weather('Turbulence')
Hailstorm = Weather('Hailstorm')
Sandstorm = Weather('Sandstorm')


class Environment:
    weather = NoWeather
