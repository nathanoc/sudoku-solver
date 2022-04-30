from inputoutput import inputGrid, outputGrid
from solver import solveGrid

def main():
    grid = inputGrid()
    solvedGrid = solveGrid(grid)
    outputGrid(solvedGrid)

main()