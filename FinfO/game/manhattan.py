from typing import List, Tuple


def move1(players: List[Tuple[int, int]], loot: List[Tuple[int, int]]) -> Tuple[int, int]:
    x, y = players[0]
    min_distance = float('inf')
    best_star = (-1, -1)

    for star in loot:
        delta_x = star[0] - x
        delta_y = star[1] - y
        lenght = abs(delta_x) + abs(delta_y)
        if lenght < min_distance:
            min_distance = lenght
            best_star = star

    if best_star[0] == x:
        if best_star[1] > y:
            return (x, y + 1)
        else:
            return (x, y - 1)

    else:
        if best_star[0] > x:
            return (x + 1, y)
        else:
            return (x -1, y)

