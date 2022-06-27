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


def zeros(n: int) -> int:
    """ find trailing zeros in factorial of a number"""
    output = 0

    while n >= 5:
        n = n // 5
        output += n

    return output


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(12) == 2
assert zeros(30) == 7
assert zeros(1000) == 249
assert zeros(100000000) == 24999999
assert zeros(10000000000000000) == 2499999999999996
assert zeros(100000000000000000000000000000000) == 24999999999999999999999999999992
