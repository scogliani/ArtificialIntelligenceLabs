# -*- coding: utf-8 -*-

import abc
from typing import List, Tuple
from collections import deque


class Strategy(metaclass=abc.ABCMeta):
    def __init__(self, _data_structure):
        self._data_structure = _data_structure

    def add(self, e) -> None:
        self._data_structure.append(e)

    @abc.abstractmethod
    def remove(self) -> List[Tuple[int, int]]:
        pass

    def empty(self) -> bool:
        return len(self._data_structure) == 0


class Stack(Strategy):
    def __init__(self):
        super().__init__(list())

    def remove(self) -> List[Tuple[int, int]]:
        return self._data_structure.pop()


class Queue(Strategy):
    def __init__(self):
        super().__init__(deque())

    def remove(self) -> List[Tuple[int, int]]:
        return self._data_structure.popleft()
