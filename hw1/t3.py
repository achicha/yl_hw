"""
Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:

Будьте осторожны 1000! имеет 2568 цифр.

Доп. инфо: http://mathworld.wolfram.com/Factorial.html

zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
"""

from typing import List


def prime_factors(n: int) -> List[int]:
    """find prime factors of number"""
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans


def zeros(n: int) -> int:
    """ find trailing zeros in factorial of a number"""

    # factorial(N) = product of numbers [2...N]
    factorial_numbers = list(range(2, n+1))

    # prime factors of each factorial's number
    prime_numbers = []
    for num in factorial_numbers:
        prime_numbers += prime_factors(num)

    # trailing zeros in factorial's product are produced by 2 and 5.
    output = min(prime_numbers.count(2), prime_numbers.count(5))
    return output


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
assert zeros(12) == 2
