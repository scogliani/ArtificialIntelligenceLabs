# Search Strategies

In this first lab assignment you will take a look at search algorithms to find
a path through a labyrinth. Such a path can be described as a list of
(x,y)-coordinates.
Start by download `labyrinth.tgz` from the eLearning platform. This file
contains a sample of labyrinth for these exercises.

## Exercise 1 - Utility functions
1. Write a first function that takes a labyrinth matrix like the one in
Figure 1 as argument and draws it using the characters `##` for walls and two
spaces for passages. This function should also accept a list of (x,y) tuples
that represent positions visited by a robot in the labyrinth, you should print
the character '.' at these points.

```
labyrinth =\
[[0,0,0,0,0,0,1,0],
 [0,1,0,1,1,1,1,0],
 [0,1,1,1,0,1,0,0],
 [0,1,0,0,0,0,0,0],
 [0,1,1,0,1,1,1,0],
 [0,0,1,1,1,0,0,0],
 [0,1,1,0,1,1,1,0],
 [0,1,0,0,0,0,0,0]]
````

2. Write a second function `adjacent_passages` that takes a labyrinth matrix
like the one above and the x and y coordinates for a place in the labyrinth as
arguments, and returns a list of the coordinates (tuples of x and y) of all
adjacent places (in 4 connexity) that are passages (i.e., have value 1). For
instance:

```
>>> adjacent_passages(labyrinth, 1, 1)
[(1, 2)]
>>> adjacent_passages(labyrinth, 6, 1)
[(6, 0), (5, 1)]
```

## Exercise 2 - Depth-first search
Write a search function that finds a way through the labyrinth. The entrance is
at (6,0) the exit at (1,15) for the labyrinth. The function should effectively
perform a depth-first search.
This can be easily done by using the search algorithm `find_path_df` from the
text "A Primer for the Labs". One of the advantages of this method is that you
have a generic search algorithm, and only need to plugin the methods for
knowing which actions you can take and detecting if you have reached the goal
or not.
Your task now is to complete this algorithm to use to perform the search
throught the labyrinth.
Don't forget to detect already visited coordinates to avoid infinite loop.

## Exercise 3 - Breadth-first search
Write a function `find_path_bg` that implements a breadth-first search using a
queue. You will only need to change a few lines of the previous algorithm for
this.

# Delivrables

At the end of the lab session, you must hand in the source code containing
exercises as a tar file sent by email
