# Sudoku Solver

Sudoku (meaning *only one single number can fit* in Japanese) is a puzzle in
a 9x9 grid so that each column, each row, and each of the nine 3x3 bowes that
compose the grid contains all of the digits from 1 to 9 (e.g., Figure 1.)
The puzzle setter provides a partially completed grid, which typically has a
unique solution

| 5 | 3 |   |   | 7 |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 6 |   |   | 1 | 9 | 5 |   |   |   |
|   | 9 | 8 |   |   |   |   | 6 |   |
| 8 |   |   |   | 6 |   |   |   | 3 |
| 4 |   |   | 8 |   | 3 |   |   | 1 |
| 7 |   |   |   | 2 |   |   |   | 6 |
|   | 6 |   |   |   |   | 2 | 8 |   |
|   |   |   | 4 | 1 | 9 |   |   | 5 |
|   |   |   |   | 8 |   |   | 7 | 9 |

| 5 | 3 | 4 | 6 | 7 | 8 | 9 | 1 | 2 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 6 | 7 | 2 | 1 | 9 | 5 | 3 | 4 | 8 |
| 1 | 9 | 8 | 3 | 4 | 2 | 5 | 6 | 7 |
| 8 | 5 | 9 | 7 | 6 | 1 | 4 | 2 | 3 |
| 4 | 2 | 6 | 8 | 5 | 3 | 7 | 9 | 1 |
| 7 | 1 | 3 | 9 | 2 | 4 | 8 | 5 | 6 |
| 9 | 6 | 1 | 5 | 3 | 7 | 2 | 8 | 4 |
| 2 | 8 | 7 | 4 | 1 | 9 | 6 | 3 | 5 |
| 3 | 4 | 5 | 2 | 8 | 6 | 1 | 7 | 9 |

---
Figure 1. Initial (left) and solved (right) Sudoku puzzle.

This kind of problem typically falls into **constraint satisfaction problem**
class.
In a first time for your development you can work with a 4x4 puzzle, to avoid
enormous search-space. The rules remain the same except that you have to place
digits from 1 to 4. Figure 2 gives you an example of such a Sudoku grid.

|   |   | 2 |   |
|:-:|:-:|:-:|:-:|
| 2 |   |   | 4 |
|   |   | 3 |   |
|   | 1 |   |   |

| 1 | 4 | 2 | 3 |
|:-:|:-:|:-:|:-:|
| 2 | 3 | 1 | 4 |
| 4 | 2 | 3 | 1 |
| 3 | 1 | 4 | 2 |
---
Figure 2. A smaller version of the Sudoku puzzle.

Download the *sudoku.tgz* file from the eLearning platform. This tar file
provides the class *Sudoku* and some grid samples. For instance the grid #4
is claimed by its creator, Finnish mathematician Arto Inkala, to be the hardest
Sudoku Puzzle.

## Exercise 1 - Problem formulation

In a text document, write a formal description of the problem, namely
variables, the domain of possible values, and the contraints. Also,
compute the total number of states for a 9x9 grid.

## Exercise 2 - The Sudoku representation

The class Sudoku (Figure 3) is defined by four methods:

| ![sudoku-class](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/scogliani/ArtificialIntelligenceLabs/main/lab3/etc/sudoku.iuml) |
|:-:|
| Figure 3. The Sudoku class. |

1. A constructor that builds a Sudoku grid of size n * n from a string with an
initial configuration (e.g., '1 3 2 4 2 ' for the grid in the Figure 2). The
grid is stored as a flat string where the index *i* in the grid is the
grid[i/n][i%n].
2. Then the method *buildDomainValues()* returns the list of the value domain
for all cells. For instance, this returns for the Figure 2 the following list:
['1234', '1234', '2', '1234', '2', '1234', '1234', '4', '1234', '1234',
 '3', '1234', '1234', '1', '1234', '1234']
3. The method *buildPendingMarks()* returns a list of the initial variable
settings with the given values. For instance, it returns for Figure 2:
[(2, '2'), (4, '2'), (7, '4'), (10, '3'), (13, '1')]
4. Finally, the method *getFriendCells()* returns the list of cell coordinates
that are in contact with a given cell (in the same row, column and box). For
instance, the neighbors of cell 0 are:
(1, 2, 3, 4, 5, 8, 12)

## Exercise 3 - Utility function

Add a method *display()* that display the current grid as it is stored in the
class Sudoku.

## Exercise 4 - Write a naive backtracking solver

Implement the methid *solve()* that performs an uninformed depth-first search
algorithm. In the text document, draw a report with the execution time of your
search algorithm and the number of states explored before the solution was
reached on various Sudoku grids given in the *samples.py*

# Delivrable

At the end of the lab session, you must hand in the **source code** containing
exercises and the **text document** with the answers to the various questions
as a tar file sent by email.
