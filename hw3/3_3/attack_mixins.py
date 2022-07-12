from abc import ABC, abstractmethod


class SimpleAttack(ABC):
    @abstractmethod
    def attack(self):
        pass


class UltimateAttack(ABC):
    @abstractmethod
    def ultimate(self):
        pass


class Kick(SimpleAttack):
    def attack(self):
        print('Kick')


class LightSaber(SimpleAttack):
    def attack(self):
        print('bzzz bzzz')


class UnlimitedAmmoGunFire(SimpleAttack):
    def attack(self):
        print('PIU PIU')


class LaserEyes(UltimateAttack):
    def ultimate(self):
        print('Wzzzuuuup!')


class JediForce(UltimateAttack):
    def ultimate(self):
        print('mm mmm')
