"""
Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса:

2149583361 -> "128.32.10.1"
32         -> "0.0.0.32"
0          -> "0.0.0.0"
"""

import ipaddress


def int32_to_ip(int32: int) -> str:
    """ convert int32 to IP address in pure python
        IP Number = 16777216*w + 65536*x + 256*y + z
    """
    o1 = int(int32 / 16777216) % 256
    o2 = int(int32 / 65536) % 256
    o3 = int(int32 / 256) % 256
    o4 = int(int32) % 256
    ip_addr = f'{o1}.{o2}.{o3}.{o4}'
    return ip_addr


def int32_to_ip_lib(int32: int) -> str:
    """ convert int32 to IP address using https://docs.python.org/3/library/ipaddress.html """
    ip_addr = str(ipaddress.IPv4Address(int32))
    return ip_addr


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(32) == "0.0.0.32"
