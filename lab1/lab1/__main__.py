# -*- coding: utf-8 -*-

import sys

from lab1.draw_labyrinth import draw_labyrinth
from lab1.find_path_df import find_path_df
from lab1.find_path_bf import find_path_bf

def main():
  l3 = \
    [[0, 0, 0, 0, 0, 0, 1, 0],
     [0, 1, 0, 1, 1, 1, 1, 0],
     [0, 1, 1, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 1, 1, 1, 0],
     [0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 1, 1, 0],
     [0, 1, 0, 0, 0, 0, 0, 0]]

  print(draw_labyrinth(l3, find_path_df(l3, (6, 0), (1, 7))))
  print(draw_labyrinth(l3, find_path_bf(l3, (6, 0), (1, 7))))

  return 0

if __name__ == "__main__":
  main()
