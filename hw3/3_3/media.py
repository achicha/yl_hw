from abc import ABC, abstractmethod

from places import Place


class Media(ABC):
    @abstractmethod
    def create_news(self, hero_name: str, place: Place):
        pass


class TV(Media):
    def create_news(self, hero_name: str, place: Place):
        print(f'{hero_name} saved the {place}! check TV channel')


class NewsPapers(Media):
    def create_news(self, hero_name: str, place: Place):
        print(f'{hero_name} saved the {place}! more in morning NewsPapers')
