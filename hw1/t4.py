"""
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.

(Используйте - для обозначения зачеркнутой буквы)
"""

from itertools import combinations
from typing import Set


def bananas(s: str) -> Set[str]:
    """find all «banana» occurrences in input string"""
    result = []
    base = 'banana'

    skipped_letters = len(s) - len(base)
    if skipped_letters == 0:
        if s == base:
            result.append(base)
        return set(result)

    indices = combinations(range(len(s)), skipped_letters)
    for ind in indices:
        res = []
        for i, v in enumerate(s):
            if i not in ind:
                res.append(v)
            else:
                res.append('-')

        output = ''.join(res)
        if output.replace("-", "") == base:
            result.append(output)

    return set(result)


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {
    "b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a", "b-ana--na",
    "b---anana", "-bana--na", "-ba--nana", "b-anan--a", "-ban--ana", "b-anana--"
}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
