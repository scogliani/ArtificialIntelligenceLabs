# -*- coding: utf-8 -*-

from typing import List, Tuple


def adjacent_passages(labyrinth: List[List[int]], y: int, x: int) \
        -> List[Tuple[int, int]]:

    ret = []

    # Left
    if 0 <= y - 1 and labyrinth[x][y - 1] == 1:
        ret.append((y - 1, x))
    # Right
    if y + 1 < len(labyrinth[0]) and labyrinth[x][y + 1] == 1:
        ret.append((y + 1, x))
    # Top
    if 0 <= x - 1 and labyrinth[x - 1][y] == 1:
        ret.append((y, x - 1))
    # Bottom
    if x + 1 < len(labyrinth) and labyrinth[x + 1][y] == 1:
        ret.append((y, x + 1))

    return ret
