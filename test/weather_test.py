import core.type as t
import core.weather as weather
from core.move import *
from core.move.weatherball import WeatherBall
from core.move.solarbeam import SolarBeam


def test_sunny_decrease_water_power():
    move = SpecialAttack()
    move.type = t.Water
    move.power = 100
    weather.adjust('Sunny', move)
    assert move.power == 50


def test_sunny_increase_fire_power():
    move = SpecialAttack()
    move.type = t.Fire
    move.power = 100
    weather.adjust('Sunny', move)
    assert move.power == 150


def test_sunny_change_weather_ball():
    move = WeatherBall()
    weather.adjust('Sunny', move)
    assert move.power == 100
    assert move.type == t.Fire


def test_rain_increase_water_power():
    move = SpecialAttack()
    move.type = t.Water
    move.power = 100
    weather.adjust('Rain', move)
    assert move.power == 150


def test_rain_decrease_fire_power():
    move = SpecialAttack()
    move.type = t.Fire
    move.power = 100
    weather.adjust('Rain', move)
    assert move.power == 50


def test_rain_decrease_solar_beam():
    move = SolarBeam()
    weather.adjust('Rain', move)
    assert move.power == 60


def test_rain_change_weather_ball():
    move = WeatherBall()
    weather.adjust('Rain', move)
    assert move.power == 100
    assert move.type == t.Water


def test_drought_even_decrease_water_power():
    move = SpecialAttack()
    move.type = t.Water
    move.power = 100
    weather.adjust('Drought', move)
    assert move.power == 0


def test_heavy_rain_even_decrease_fire_power():
    move = SpecialAttack()
    move.type = t.Fire
    move.power = 100
    weather.adjust('Heavy Rain', move)
    assert move.power == 0


def test_hail_decrease_solar_beam():
    move = SolarBeam()
    weather.adjust('Hail', move)
    assert move.power == 60


def test_hail_change_weather_ball():
    move = WeatherBall()
    weather.adjust('Hail', move)
    assert move.power == 100
    assert move.type == t.Ice


def test_sandstorm_decrease_solar_beam():
    move = SolarBeam()
    weather.adjust('Sandstorm', move)
    assert move.power == 60


def test_sandstorm_change_weather_ball():
    move = WeatherBall()
    weather.adjust('Sandstorm', move)
    assert move.power == 100
    assert move.type == t.Rock
