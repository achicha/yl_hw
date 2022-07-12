"""
Надо написать декоратор для повторного выполнения декорируемой функции через некоторое время.
Использует наивный экспоненциальный рост времени повтора (factor) до граничного времени ожидания (border_sleep_time).

В качестве параметров декоратор будет получать:
call_count - число, описывающее кол-во раз запуска функций;
start_sleep_time - начальное время повтора;
factor - во сколько раз нужно увеличить время ожидания;
border_sleep_time - граничное время ожидания.

Формула:
t = start_sleep_time * 2^(n) if t < border_sleep_time
t = border_sleep_time if t >= border_sleep_time
"""
import time
from typing import Callable


def retry(call_count, start_sleep_time, factor, boarder_sleep_time):
    """
        Retry decorator that repeats function call with delay.

    :param call_count: how many times should run callable func
    :param start_sleep_time: retry start time
    :param factor: multiplier to increase delay time between retries
    :param boarder_sleep_time: maximum delay time
    :return:
    """
    def my_decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            print(f'Количество запусков = {call_count}')
            print('Начало работы')
            time_start = time.perf_counter()

            for n in range(1, call_count+1):
                t = min(start_sleep_time * factor ** n, boarder_sleep_time)
                time.sleep(t)
                result = func(n, t, *args, **kwargs)
                print(f'Запуск номер {n}. Ожидание: {t} секунд. Результат декорируемой функций = {result}.')

            time_end = time.perf_counter()
            time_total = round(time_end - time_start)
            print(f'Конец работы. Время выволнения {time_total} секунды.')
        return wrapper
    return my_decorator


@retry(call_count=10, start_sleep_time=1, factor=1.2, boarder_sleep_time=3)
def my_func(x: int, y: float) -> float:
    """Multiply X by Y"""
    return x * y


if __name__ == '__main__':
    my_func()
