from operator import itemgetter
from typing import List, Tuple


def find_way(point1: Tuple[int, int], point2: Tuple[int, int]):
    output = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
    return output


def sort_points(points, start):
    output = []
    while points:
        dct = {find_way(x, start): x for x in points}
        point_next = points.pop(points.index(dct[min(dct.keys())]))
        output.append(point_next)
        start = point_next
    return output


def shortest_way(points: List[Tuple[int, int]]):
    # starting point
    point_start = points.pop(0)

    # find the shortest route between all others points
    points_route = sort_points(points, point_start)

    point_next = None
    sum_lines = 0
    output = []

    while points_route:
        point_prev = point_next if point_next else point_start
        point_next = points_route.pop(0)
        line = find_way(point_next, point_prev)
        sum_lines += line
        output.append((point_next, sum_lines))

    # from last to start
    sum_lines += find_way(point_next, point_start)
    output.append((point_start, sum_lines))

    return str(point_start) + ' -> ' + ' -> '.join([f'{x[0]}[{x[1]}]' for x in output]) + ' = ' + str(sum_lines)


# assert shortest_way([(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]) == '(0, 2) -> (2, 5)[3.605551275463989] -> (6, 6)[7.728656901081649] -> (8, 3)[11.334208176545639] -> (5, 2)[14.496485836714019] -> (0, 2)[19.49648583671402] = 19.49648583671402'


res = shortest_way([(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)])
print(res)