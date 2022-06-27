"""
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.

(Используйте - для обозначения зачеркнутой буквы)
"""

from typing import Set


def bananas(s: str, obj: str = 'banana') -> Set[str]:
    """find all «banana» occurrences in input string. recursive approach"""
    output = set()

    if obj == '':
        output.add(''.rjust(len(s), '-'))
        return output

    for i in range(len(s)):
        if obj[0] == s[i]:
            left_part = ''.rjust(i, '-') + s[i]

            if s[i + 1:] == '' and obj[1:] == '':
                output.add(left_part)
            else:
                right_parts = bananas(s[i + 1:], obj[1:])
                for right_part in right_parts:
                    output.add(left_part + right_part)
    return output


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {
    "b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a", "b-ana--na",
    "b---anana", "-bana--na", "-ba--nana", "b-anan--a", "-ban--ana", "b-anana--"
}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

assert isinstance(bananas("bbbbananabbbbnnanananananannsssaaaannannnannaaassss"), set)
assert len(bananas("bbbbananabbbbnnanananananannsssaaaannannnannaaassss")) > 1000

