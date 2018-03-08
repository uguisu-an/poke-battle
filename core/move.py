# class Move:
#     def __init__(self, source, target, environment=None):
#         self.source = source
#         self.target = target
#         self.environment = environment
#
#     def doit(self):
#         pass


class Attack:
    type = None

    def type_match(self, monster_type):
        return monster_type.match(self.type)


class PhysicalAttack(Attack):
    @staticmethod
    def select_attack(attacker):
        return attacker.py_atk

    @staticmethod
    def select_defence(defender):
        return defender.py_def


class SpecialAttack(Attack):
    @staticmethod
    def select_attack(attacker):
        return attacker.sp_atk

    @staticmethod
    def select_defence(defender):
        return defender.sp_def


class Move:
    def select_attack(self, attacker):
        return 0

    def select_defence(self, defender):
        return 0


# TODO: NoneType作る？
class NormalMove(Move):
    def __init__(self, power=0, move_type=None, name=''):
        self.name = name
        self.power = power
        self.type = move_type

    def select_attack(self, attacker):
        return attacker['atk']

    def select_defence(self, defender):
        return defender['def']


class SpecialMove(Move):
    def __init__(self, power=0, move_type=None, name=''):
        self.name = name
        self.power = power
        self.type = move_type

    def select_attack(self, attacker):
        return attacker['sp.atk']

    def select_defence(self, defender):
        return defender['sp.def']
