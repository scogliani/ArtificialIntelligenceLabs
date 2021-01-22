# -*- coding: utf-8 -*-

from typing import List, Tuple

from .FindPathTemplateMethod import FindPathStack


def find_path_df(labyrinth: List[List[int]], entrance: Tuple[int, int],
                 exit: Tuple[int, int]) -> List[Tuple[int, int]]:
    return FindPathStack(labyrinth, entrance, exit).find_path()
