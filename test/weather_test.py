import core.type as t
import core.weather as weather


def test_sunny_adjust_damage():
    assert weather.adjust('Sunny', 100, t.Water) == 50
    assert weather.adjust('Sunny', 100, t.Normal) == 100
    assert weather.adjust('Sunny', 100, t.Fire) == 150


def test_sunny_adjust_thunder_accuracy():
    assert weather.adjust_accuracy('Sunny', 'Pound') == 1.0
    assert weather.adjust_accuracy('Sunny', 'Thunder') == 0.5
    assert weather.adjust_accuracy('Sunny', 'Hurricane') == 0.5


def test_rain_adjust_damage():
    assert weather.adjust('Rain', 100, t.Fire) == 50
    assert weather.adjust('Rain', 100, t.Normal) == 100
    assert weather.adjust('Rain', 100, t.Water) == 150

