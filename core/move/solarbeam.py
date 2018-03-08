from core.type import Grass
from core.move import SpecialAttack


# TODO: こちら側で自発的に天気の影響を受ける？
class SolarBeam(SpecialAttack):
    name = 'Solar Beam'
    type = Grass
    power = 120
