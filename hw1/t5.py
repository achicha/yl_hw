"""
Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
предел (limit), после чего попробуйте сгенерировать по порядку все числа.
Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.

primesL = [2, 5, 7]
limit = 500
List of Numbers Under 500          Prime Factorization
___________________________________________________________
           70                         [2, 5, 7]
          140                         [2, 2, 5, 7]
          280                         [2, 2, 2, 5, 7]
          350                         [2, 5, 5, 7]
          490                         [2, 5, 7, 7]
5 из этих чисел меньше 500, а самое большое из них 490.
"""

from typing import List


def count_find_num(primesL: List[int], limit: int) -> List:
    """
    1. find count of possible products that less then limit
    2. find max of found products
    """
    products = []

    # product of all given prime numbers
    base = 1
    for p in primesL:
        base *= p
    if base < limit:
        products.append(base)
    else:
        return products

    # find all products
    def f(nums, output, end):
        for j in output:
            for i in nums:
                n = j * i
                if n <= end:
                    if n not in output:
                        output.append(n)
    f(primesL, products, limit)

    return [len(products), max(products)]


assert count_find_num([2, 5, 7], 500) == [5, 490]
assert count_find_num([2, 3], 200) == [13, 192]
assert count_find_num([2, 5], 200) == [8, 200]
assert count_find_num([2, 3, 5], 500) == [12, 480]
assert count_find_num([2, 3, 5], 1000) == [19, 960]
assert count_find_num([2, 3, 47], 200) == []
