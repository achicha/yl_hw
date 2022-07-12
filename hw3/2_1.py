"""
Надо написать класс CyclicIterator.
Итератор должен итерироваться по итерируемому объекту (list, tuple, set, range, Range2, и т. д.),
и когда достигнет последнего элемента, начинать сначала.

Ref:
https://university.ylab.site/python/iterators/
https://stackoverflow.com/questions/56237021/iterable-class-in-python3
"""
from typing import Iterable, Iterator


class CyclicIterator:
    def __init__(self, ids: Iterable):
        self.ids: Iterable = ids
        self.iterator: Iterator = iter(self.ids)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.ids)
            return next(self.iterator)


if __name__ == '__main__':
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
