# Genetic Queens

## Introduction

This project aim to solve the problem of placing n queens in a n-sized chess board using genetic algorithm.
We start with a population of k boards.

Each generetion we produce k new boards and mantain the best to the next generation.

Each generated board has a chance m of being mutaded.

## Dependencies

To run this project, you will need Python3 and Pygame installed.

## How to run

You can run this project by cloning it and running `python3 main.py`.

It will by default run the simulation for a board with size n = 50, a population with size k = 40 and a mutation chance m = 0.5.

You can also set this parameters when running the project at this order: `python3 main.py n m k`

For example, running:

```
python3 main.py 20 30 0.3
``` 

will run the simulation with values `n = 20; k = 30; m = 0.3`

The restrictions are: 
- n can be 15, 20, 30 or 50
- k must be even
- m must be `0 < m < 1`
