class NormalMove:
    def __init__(self, power):
        self._power = power

    def _select_attack(self, attacker):
        return attacker['atk']

    def _select_defence(self, defender):
        return defender['def']

    def _revision(self, attacker, defender):
        return self._select_attack(attacker) / self._select_defence(defender)

    def damage(self, attacker, defender):
        return self._power * self._revision(attacker, defender)


class SpecialMove(NormalMove):
    def _select_attack(self, attacker):
        return attacker['sp.atk']

    def _select_defence(self, defender):
        return defender['sp.def']
