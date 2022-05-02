# sudoku-solver

## Summary
This is a sudoku solver (two sudoku solvers, actually) that I put together over the course of a few evenings. One is an algorithm that I came up with myself, and is basically just the way I play sudoku, by going through every row, column and box and seeing if there are any squares that can only be one number, and filling those in until the whole puzzle is filled (more detail in the Bad Solver section). As it turns out this doesn't work for most harder sudokus, hence the second algorithm: the backtracking algorithm, a.k.a. the first algorithm that comes up when you google "sudoku solver algorithm". Though the algorithm isn't mine, the implementation is (see the Backtracking Solver section). It basically works by filling in squares until it gets stuck, and then going back and adjusting things until they do work.

## Bad Solver
### Algorithm Summary
The program repeatedly loops through every box in the grid, making a list of all the possible numbers that could go in each square. If there is only one possible number for a square, it fills that square in. It repeats until either the board is filled or it reaches a hard-coded iteration limit.
### Code
The code is divided across five files, which turned out to be massively unnecessary. These are [gridManipulation.py](bad-solver/gridManipulation.py), [inputoutput.py](bad-solver/inputoutput.py), [main.py](bad-solver/main.py), [solver.py](bad-solver/solver.py), and [validity.py](bad-solver/validity.py).

## Backtracking Solver
### Algorithm Summary
The program begins at the top-left box, and increments its value until it fits. It then moves on to the next square and does the same, until it reaches a square where no number can fit. At this point the program backtracks (hence its name) until it finds a square that can be adjusted, and then makes its way forward again, backtracking where necessary, until the whole puzzle is filled in.
### Code
Having learned my lesson from making the bad solver, I put all the code for this algorithm into one file - [solver.py](backtracking-solver/solver.py). When I made that decision I thought I might end up regretting it:

```python
# all in one file; might regret this later.
```

In the end, though, it caused me no problems at all, and partially for this reason I found this algorithm a lot easier to work with than the bad solver.
