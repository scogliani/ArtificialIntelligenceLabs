# -*- coding: utf-8 -*-

from typing import List, Tuple

from .FindPathTemplateMethod import FindPathQueue


def find_path_bf(labyrinth: List[List[int]], entrance: Tuple[int, int],
                 exit: Tuple[int, int]) -> List[Tuple[int, int]]:
    return FindPathQueue(labyrinth, entrance, exit).find_path()
