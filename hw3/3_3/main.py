from typing import List, Union

from media import Media, TV, NewsPapers
from places import Place, Kostroma, Tokyo, Tatooine
from heroes import Hero, SuperHero, Superman, ChuckNorris, LukeSkywalker, SupermanName


def save_the_place(hero: Union[Hero, SuperHero], place: Place, medias: List[Media]):
    place.get_antagonist()
    hero.attack()
    if hero.can_use_ultimate_attack():
        hero.ultimate()
    for media in medias:
        media.create_news(hero.get_name(), place)


if __name__ == '__main__':
    save_the_place(Superman(name=SupermanName.Superman), Kostroma(), [TV(), NewsPapers()])
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), [TV()])
    print('-' * 20)
    save_the_place(LukeSkywalker(), Tatooine(), [NewsPapers()])
