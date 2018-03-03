import core.type as t
import core.weather as weather
from core.move import SpecialMove


def test_sunny_decrease_water_power():
    move = SpecialMove(100, t.Water)
    weather.adjust('Sunny', move)
    assert move.power == 50


def test_sunny_increase_fire_power():
    move = SpecialMove(100, t.Fire)
    weather.adjust('Sunny', move)
    assert move.power == 150


def test_sunny_change_weather_ball():
    move = SpecialMove(50, t.Normal, 'Weather Ball')
    weather.adjust('Sunny', move)
    assert move.power == 100
    assert move.type == t.Fire


def test_rain_increase_water_power():
    move = SpecialMove(100, t.Water)
    weather.adjust('Rain', move)
    assert move.power == 150


def test_rain_decrease_fire_power():
    move = SpecialMove(100, t.Fire)
    weather.adjust('Rain', move)
    assert move.power == 50


def test_rain_decrease_solar_beam():
    move = SpecialMove(120, t.Grass, 'Solar Beam')
    weather.adjust('Rain', move)
    assert move.power == 60


def test_rain_change_weather_ball():
    move = SpecialMove(50, t.Normal, 'Weather Ball')
    weather.adjust('Rain', move)
    assert move.power == 100
    assert move.type == t.Water
