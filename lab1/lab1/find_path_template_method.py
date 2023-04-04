# -*- coding: utf-8 -*-

import abc
from typing import List, Tuple
from collections import deque

from .adjacent_passages import adjacent_passages
from .strategy import Strategy


class FindPathTemplateMethod(metaclass=abc.ABCMeta):
    def __init__(
        self, __labyrinth: List[List[int]],
            __begin: Tuple[int, int],
            __end: Tuple[int, int]):
        self.__labyrinth = __labyrinth
        self.__begin = __begin
        self.__end = __end

    def find_path(self) -> List[Tuple[int, int]]:
        ds = self.data_structure_strategy()

        visited = list()
        ds.add([self.__begin])
        while not ds.empty():
            path = ds.remove()
            position = path[-1]

            if position == self.__end:
                return path[1:]

            visited.append(position)
            for e in adjacent_passages(self.__labyrinth, *position):
                if e not in visited:
                    ds.add(path + [e])

        return [(-1, -1)]

    @abc.abstractmethod
    def data_structure_strategy(self) -> Strategy:
        pass
