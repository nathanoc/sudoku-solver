# all in one file; might regret this later.

# imports

from math import *

# input sudoku

linearGrid = []
print("Enter the full puzzle. Use 0 for blank squares. Do not add any spaces, line breaks, or commas - just enter one long string of numbers. The width of the puzzle must be a perfect square.")
gridString = input()
for num in gridString:
    linearGrid.append(int(num))

puzzleWidth = int(sqrt(len(linearGrid)))

# various board functions

def getRows():
    rows = []
    for i in range(puzzleWidth):
        rows.append(linearGrid[(i * puzzleWidth):(i * puzzleWidth + puzzleWidth)])
    return rows

def getColumns():
    columns = []
    for i in range(puzzleWidth):
        columns.append([])
    
    for i in range(len(linearGrid)):
        columns[i % puzzleWidth].append(linearGrid[i])
    
    return columns

def getBoxes():
    boxes = []
    for i in range(puzzleWidth):
        boxes.append([])

    boxesPerRow = int(sqrt(puzzleWidth))

    for row in range(puzzleWidth):
        for column in range(puzzleWidth):
            boxes[floor(column / boxesPerRow) + (boxesPerRow * floor(row / boxesPerRow))].append(linearGrid[(row * puzzleWidth) + column])
    
    return boxes

# function to check if the puzzle is valid (i.e. no duplicates on any row)

def checkValid():
    rows = getRows()
    columns = getColumns()
    boxes = getBoxes()
    for checkNum in range(1, puzzleWidth + 1):
        for sectionIndex in range(puzzleWidth):
            if rows[sectionIndex].count(checkNum) > 1:
                return False
            if columns[sectionIndex].count(checkNum) > 1:
                return False
            if boxes[sectionIndex].count(checkNum) > 1:
                return False
    return True

# get indices of empty squares

empties = []
for i in range(len(linearGrid)):
    if linearGrid[i] == 0:
        empties.append(i)

# solve the grid

emptiesIndex = 0
iterations = 0
while linearGrid.count(0) != 0:
    boardIndex = empties[emptiesIndex]

    while (linearGrid[boardIndex] == 0 or checkValid() == False) and linearGrid[boardIndex] <= 9:
        linearGrid[boardIndex] += 1

    if linearGrid[boardIndex] > 9:
        linearGrid[boardIndex] = 0
        emptiesIndex -= 1
        boardIndex = empties[emptiesIndex]
        linearGrid[boardIndex] += 1
    else:
        emptiesIndex += 1
    
    iterations += 1
    if iterations % 1000 == 0:
        print(str(iterations) + " \titerations")

# output the grid

for row in getRows():
    for square in row:
        print(str(square), end = "")
    print()