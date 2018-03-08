import core.type as t
from core.effect.weather import *
from core.move import *
from core.move.weatherball import WeatherBall
from core.move.solarbeam import SolarBeam


def test_sunny_decrease_water_power():
    move = SpecialAttack()
    move.type = t.Water
    move.power = 100
    adjust('Sunny', move)
    assert move.power == 50


def test_sunny_increase_fire_power():
    move = SpecialAttack()
    move.type = t.Fire
    move.power = 100
    adjust('Sunny', move)
    assert move.power == 150


def test_rain_increase_water_power():
    move = SpecialAttack()
    move.type = t.Water
    move.power = 100
    adjust('Rain', move)
    assert move.power == 150


def test_rain_decrease_fire_power():
    move = SpecialAttack()
    move.type = t.Fire
    move.power = 100
    adjust('Rain', move)
    assert move.power == 50


def test_drought_even_decrease_water_power():
    move = SpecialAttack()
    move.type = t.Water
    move.power = 100
    adjust('Drought', move)
    assert move.power == 0


def test_heavy_rain_even_decrease_fire_power():
    move = SpecialAttack()
    move.type = t.Fire
    move.power = 100
    adjust('Heavy Rain', move)
    assert move.power == 0


def test_sunny_change_weather_ball():
    move = WeatherBall()
    move.affected_by(Sunny)
    assert move.power == 100
    assert move.type == t.Fire


def test_rainy_decrease_solar_beam():
    move = SolarBeam()
    move.affected_by(Rainy)
    assert move.power == 60

