# -*- coding: utf-8 -*-

import abc
from typing import List, Tuple
from collections import deque

from .adjacent_passages import adjacent_passages


class Strategy(metaclass=abc.ABCMeta):
  def __init__(self, _data_structure):
    self.__dict__.update(
        {k: v for k, v in locals().items() if k != "self"})

  def add(self, e):
    self._data_structure.append(e)

  @abc.abstractmethod
  def remove(self):
    pass

  def empty(self):
    return len(self._data_structure) == 0


class Stack(Strategy):
  def __init__(self):
    super().__init__(list())

  def remove(self):
    return self._data_structure.pop()


class Queue(Strategy):
  def __init__(self):
    super().__init__(deque())

  def remove(self):
    return self._data_structure.popleft()


class FindPathTemplateMethod(metaclass=abc.ABCMeta):
  def __init__(self, __labyrinth: List[List[int]], __exit: Tuple[int, int]):
    self.__dict__.update(
        {k: v for k, v in locals().items() if k != "self"})

  def find_path(self,
                position: Tuple[int, int],
                visited: List[Tuple[int, int]] = None,
                path: List[Tuple[int, int]] = None) -> List[Tuple[int, int]]:
    if visited is None:
      visited = []

    if path is None:
      path = []

    visited.append(position)
    path.append(position)

    ds = self.data_structure_strategy()
    for e in adjacent_passages(self.__labyrinth, *position):
      if e not in visited:
        ds.add(e)

    while not ds.empty():
      e = ds.remove()

      self.find_path(e, visited, path)

      if self.__exit in path:
        break

    return path

  @abc.abstractmethod
  def data_structure_strategy(self) -> Strategy:
    pass


class FindPathStack(FindPathTemplateMethod):
  def data_structure_strategy(self) -> Strategy:
    return Stack()


class FindPathQueue(FindPathTemplateMethod):
  def data_structure_strategy(self) -> Strategy:
    return Queue()
