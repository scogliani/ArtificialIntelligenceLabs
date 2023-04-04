# -*- coding: utf-8 -*-

from typing import List, Tuple

from .find_path_template_method import (
        FindPathTemplateMethod
)
from .strategy import (
        Stack, Strategy
)


class FindPathDFS(FindPathTemplateMethod):
    def data_structure_strategy(self) -> Strategy:
        return Stack()


def find_path_df(labyrinth: List[List[int]], entrance: Tuple[int, int],
                 exit: Tuple[int, int]) -> List[Tuple[int, int]]:
    return FindPathDFS(labyrinth, entrance, exit).find_path()
