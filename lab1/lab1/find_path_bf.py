# -*- coding: utf-8 -*-

from typing import List, Tuple

from .find_path_template_method import (
        FindPathTemplateMethod
)
from .strategy import (
        Queue, Strategy
)


class FindPathBFS(FindPathTemplateMethod):
    def data_structure_strategy(self) -> Strategy:
        return Queue()


def find_path_bf(labyrinth: List[List[int]], entrance: Tuple[int, int],
                 exit: Tuple[int, int]) -> List[Tuple[int, int]]:
    return FindPathBFS(labyrinth, entrance, exit).find_path()
