"""
У каждого фильма есть расписание, по каким дням он идёт в кинотеатрах.
Для эффективности дни проката хранятся периодами дат.
Например, прокат фильма проходит с 1 по 7 января, а потом показ возобновляется с 15 января по 7 февраля:
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        """ Dates when movie is shown."""
        for date_range in self.dates:
            first_date: datetime = date_range[0]
            dates_count: int = (date_range[1] - date_range[0]).days
            all_dates: Generator[datetime, None, None] = (first_date + timedelta(days=x) for x in range(dates_count+1))
            for date in all_dates:
                yield date


if __name__ == '__main__':
    m = Movie('sw', [
      (datetime(2020, 1, 1), datetime(2020, 1, 7)),
      (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)
