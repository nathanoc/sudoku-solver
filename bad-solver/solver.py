from gridManipulation import getBoxes, getColumns, getRows, getBoxIndex, getColumnIndex, getRowIndex
from validity import isValid

from inputoutput import outputGrid # only for testing

def isSolved(linearGrid):
    for i in linearGrid:    # check for empty squares
        if i == 0:  # 0 = empty square
            return False

    if isValid(linearGrid):
        return True
    else:
        return False

def getPossibilities(linearGrid):
    possibilities = []

    boxes = getBoxes(linearGrid)
    columns = getColumns(linearGrid)
    rows = getRows(linearGrid)
    
    for squareIndex in range(81):
        possibilities.append([])
        if linearGrid[squareIndex] != 0:
            continue    # its possibilities can be left empty

        theoreticalPossibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        box = boxes[getBoxIndex(squareIndex)]
        for boxMember in box:
            if boxMember in theoreticalPossibilities:
                theoreticalPossibilities.remove(boxMember)
        
        row = rows[getRowIndex(squareIndex)]
        for rowMember in row:
            if rowMember in theoreticalPossibilities:
                theoreticalPossibilities.remove(rowMember)

        column = columns[getColumnIndex(squareIndex)]
        for columnMember in column:
            if columnMember in theoreticalPossibilities:
                theoreticalPossibilities.remove(columnMember)
        
        possibilities[squareIndex] = theoreticalPossibilities
    
    return possibilities


def solveGrid(linearGrid):
    iterations = 0
    while not isSolved(linearGrid):
        allPossibilities = getPossibilities(linearGrid)
        for squareIndex in range(81):
            squarePossibilities = allPossibilities[squareIndex]
            if len(squarePossibilities) == 1:
                linearGrid[squareIndex] = squarePossibilities[0]    # fill in the empty square with its value
        iterations += 1
        if iterations > 10000: # this number is arbitrary
            print("Unsolvable by this algorithm")
            return
        
    print("Solved")
    return linearGrid

