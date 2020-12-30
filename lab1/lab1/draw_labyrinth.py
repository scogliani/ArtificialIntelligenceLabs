# -*- coding: utf-8 -*-

from typing import List, Tuple


def draw_labyrinth(labyrinth: List[List[int]], path: List[Tuple[int, int]]
                   ) -> str:
  """! Output a labyrinth integer matrix to a terminal with '##' for representing 0,
  and '  ' for representing 1. A path is also draw from the path (represented
  by '. '
  @param labyrinth A list of list representing a labyrinth matrix
  @param path A list representing the way used

  @return The matrix drawn
  """
  return "".join(
          ["".join(
            [". " if (j, i) in path else "##" if col == 0 else "  "
              for j, col in enumerate(row)
            ] + ["\n"]
            ) for i, row in enumerate(labyrinth)
          ]
        )
