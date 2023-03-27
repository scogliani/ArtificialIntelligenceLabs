# Search Strategies (Continuation)

This second lab assignment is the continuation of the first lab.
We will add new search strategies and draw a comparison of the different
implemented strategies

## Exercise 1 - Iterative deepening algorithm
Write a new version of the depth-first search using iterative deepening.
This can easy be made by adding a loop around the depth-first search
algorithm.

## Exercise 2 - Greedy best-first search
Write a best-first search algorithm. For this, you should find an
**admissible** heuristics. Does your algorithm generate an optimal solution?

## Exercise 3 - A* search
Finally, you should write a new function that performs an A* search through
the labyrinth. For this, you could reuse the **admissible** heuristics of the
previous exercise.

## Exercise 4 - Comparing the search algorithms
Investigate the different order in which the neighbors of a position is
returned by your function **adjacent_passages**.

1. Based on the result, compute how many modes theoretically were visited
during the depth, respectively breadth-first search. Also compute/estimate
the maximum amount of memory used by the different versions of the algorithms.

2. Does the greedy best-first and A* algorithms generate an optimal solution?

3. Which method(s) was faster and which method(s) yielded the shortest path?

4. Run all algorithms and draw a table with the results in terms of execution
time, number of steps and cost. Compare the results with your theoretical
results and give conclusions.

# Delivrables

At the end of the lab session, you must hand in the **source code** containing
exercises as a tar file sent by email.
Before the next lab session, you must hand in a separate **report** with the
answers to the question of the exercise 4
