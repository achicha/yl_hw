from enum import Enum
from abc import ABC, abstractmethod

from attack_mixins import Kick, UnlimitedAmmoGunFire, LaserEyes, JediForce, LightSaber


class SupermanName(Enum):
    Man = 'Clark Kent'
    Superman = 'Kal-El'


class Hero(ABC):
    def __init__(self, name: str, can_use_ultimate_attack: bool = False):
        self._name = name
        self._ultimate_attack = can_use_ultimate_attack

    @abstractmethod
    def attack(self):
        pass

    def get_name(self) -> str:
        return self._name

    def can_use_ultimate_attack(self) -> bool:
        return self._ultimate_attack

    def __repr__(self):
        return self.get_name()


class SuperHero(Hero):
    def __init__(self, name: str, can_use_ultimate_attack: bool = True):
        super(SuperHero, self).__init__(name, can_use_ultimate_attack)

    @abstractmethod
    def ultimate(self):
        pass


class Superman(Kick, LaserEyes, SuperHero):
    def __init__(self, name: SupermanName = SupermanName.Superman):
        can_use_ultimate_attack = False if name == SupermanName.Man else True
        super(Superman, self).__init__(name.value, can_use_ultimate_attack)


class ChuckNorris(UnlimitedAmmoGunFire, Hero):
    def __init__(self, name='Chuck Norris'):
        super(ChuckNorris, self).__init__(name)


class LukeSkywalker(LightSaber, JediForce, SuperHero):
    def __init__(self, name='Luke Skywalker'):
        super(LukeSkywalker, self).__init__(name)

