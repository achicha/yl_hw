from abc import ABC, abstractmethod
from typing import Union, List


class Place(ABC):
    def __init__(self, name: Union[str, List[float]]):
        self._name = name

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_antagonist(self) -> str:
        pass

    def __repr__(self):
        return self.get_name()


class Kostroma(Place):
    def __init__(self):
        super(Kostroma, self).__init__('Kostroma')

    def get_name(self) -> str:
        return self._name

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    def __init__(self):
        super(Tokyo, self).__init__('Tokyo')

    def get_name(self) -> str:
        return self._name

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')


class Tatooine(Place):
    def __init__(self):
        super(Tatooine, self).__init__([296.0, -248.1])
        self._name = '; '.join([str(x) for x in self._name])

    def get_name(self) -> str:
        return f'Planet {self.__class__.__name__} [{self._name}]'

    def get_antagonist(self):
        print('Jabba the Hutt still alive')
