from typing import List, Tuple
from itertools import permutations


def find_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """find distance between two points"""
    output = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
    return output


def shortest_route(points: List[Tuple[int, int]]) -> str:
    """find the shortest route in point_start -> all other points -> point_start"""

    # first point in points list is a starting point
    point_start = points.pop(0)
    routes = []

    for route in permutations(points):
        # starting point -> first point
        total_distance = find_distance(point_start, route[0])
        route_str = f'{point_start} -> {route[0]}[{total_distance}]'
        # all middle points
        for i in range(1, len(route)):
            total_distance += find_distance(route[i-1], route[i])
            route_str += f' -> {route[i]}[{total_distance}]'
        # from last point to start
        total_distance += find_distance(point_start, route[-1])
        route_str += f' -> {point_start}[{total_distance}]'

        routes.append({'route': route_str, 'distance': total_distance})

    # find the shortest route between all points
    output = min(routes, key=lambda x: x['distance'])
    return f"{output['route']} = {output['distance']}"


assert shortest_route([(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]) == '(0, 2) -> (2, 5)[3.605551275463989] -> (6, 6)[7.728656901081649] -> (8, 3)[11.334208176545639] -> (5, 2)[14.496485836714019] -> (0, 2)[19.49648583671402] = 19.49648583671402'
assert shortest_route([(0, 2), (2, 5), (5, 2), (6, 6), (8, 3), (0, 12), (12, 0)]) == '(0, 2) -> (5, 2)[5.0] -> (12, 0)[12.280109889280517] -> (8, 3)[17.280109889280517] -> (6, 6)[20.885661164744505] -> (0, 12)[29.370942538983073] -> (2, 5)[36.65105242826359] -> (0, 2)[40.25660370372758] = 40.25660370372758'
