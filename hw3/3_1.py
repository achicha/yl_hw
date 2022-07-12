"""
Напишите функцию-декоратор, которая сохранит (закэширует) значение декорируемой функции multiplier (Чистая функция).
Если декорируемая функция будет вызвана повторно с теми же параметрами —
декоратор должен вернуть сохранённый результат, не выполняя функцию.

В качестве структуры для кэша, можете использовать словарь в Python.
*В качестве задания со звездочкой можете использовать вместо Python-словаря => Redis.
"""
from typing import Tuple, Callable


def cache_layer(func: Callable) -> Callable:
    """ Cache intermediate layer. decorator that stores input data. """
    cache = {}

    def wrapper(*args, **kwargs):
        key: int = args[0]
        if key not in cache.keys():
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@cache_layer
def multiplier(number: int) -> int:
    """ Multiplier input number by 2. """
    return number * 2


if __name__ == '__main__':
    numbers: Tuple = (1, 2, 3, 4, 4, 4, 5, 5, 5, 5)
    for n in numbers:
        print(multiplier(n))
