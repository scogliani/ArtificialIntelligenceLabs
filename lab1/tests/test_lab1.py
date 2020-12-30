import pytest

from lab1 import __version__
from lab1.draw_labyrinth import draw_labyrinth
from lab1.adjacent_passages import adjacent_passages
from lab1.find_path_df import find_path_df

def test_version():
  assert __version__ == '0.1.0'

def test_1():
  l1 = \
      [[1, 0],
       [0, 0]]

  assert draw_labyrinth(l1, [(0, 0)]) == f""". ##
####
"""

  l2 = \
      [[0, 0],
       [1, 0]]

  assert draw_labyrinth(l2, [(0, 1)]) == f"""####
. ##
"""

  l3 = \
      [[0, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 1, 1, 1, 1, 0],
       [0, 1, 1, 1, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 1, 1, 1, 0],
       [0, 0, 1, 1, 1, 0, 0, 0],
       [0, 1, 1, 0, 1, 1, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 0]]

  assert draw_labyrinth(l3, [(6, 0)]) == f"""############. ##
##  ##        ##
##      ##  ####
##  ############
##    ##      ##
####      ######
##    ##      ##
##  ############
"""

  assert draw_labyrinth(l3, [(6, 0), (6, 1), (5, 1), (4, 1), (3, 1), (3, 2),
                             (2, 2), (1, 2), (1, 3), (1, 4), (2, 4), (2, 5),
                             (2, 6), (1, 6), (1, 7)]) == f"""############. ##
##  ##. . . . ##
##. . . ##  ####
##. ############
##. . ##      ##
####.     ######
##. . ##      ##
##. ############
"""

  assert adjacent_passages(l3, 1, 1) == [(1, 2)]
  assert adjacent_passages(l3, 6, 1) == [(5, 1), (6, 0)]
  assert adjacent_passages(l3, 6, 7) == [(6, 6)]
  assert adjacent_passages(l3, 0, 1) == [(1, 1)]
  assert adjacent_passages(l3, 7, 1) == [(6, 1)]

def test_2():
  l1 = \
      [[1, 0],
       [1, 0]]

  assert find_path_df(l1, (0, 0), (0, 1)) == [(0, 0), (0, 1)]

  l2 = \
      [[1, 0, 0],
       [1, 0, 0],
       [1, 1, 1]]

  assert find_path_df(l2, (0, 0), (2, 2)) == [(0, 0), (0, 1), (0, 2),
                                                    (1, 2), (2, 2)]
