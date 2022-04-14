from math import ceil

# Functions for getting row/column/box index of a square

def getColumnIndex(squareIndex):
    squareIndex += 1    # since indices start at zero

    columnIndex = squareIndex % 9
    if columnIndex == 0:
        columnIndex = 9

    columnIndex -= 1    # back to zero-based indexing
    return columnIndex

def getRowIndex(squareIndex):
    squareIndex += 1    # since indices start at zero

    rowIndex = ceil(squareIndex / 9)

    rowIndex -= 1    # back to zero-based indexing
    return rowIndex

def getBoxIndex(squareIndex):
    columnIndex = getColumnIndex(squareIndex) + 1  # these functions work with zero-based indexing so we add 1 for readability
    rowIndex = getRowIndex(squareIndex) + 1

    squareIndex += 1    # since indices start at zero

    if columnIndex in [1, 2, 3]:
        if rowIndex in [1, 2, 3]:
            return 0    # zero-based indexing since we're just returning
        if rowIndex in [4, 5, 6]:
            return 1
        if rowIndex in [7, 8, 9]:
            return 2
        return -1
    if columnIndex in [4, 5, 6]:
        if rowIndex in [1, 2, 3]:
            return 3
        if rowIndex in [4, 5, 6]:
            return 4
        if rowIndex in [7, 8, 9]:
            return 5
        return -1
    if columnIndex in [7, 8, 9]:
        if rowIndex in [1, 2, 3]:
            return 6
        if rowIndex in [4, 5, 6]:
            return 7
        if rowIndex in [7, 8, 9]:
            return 8
        return -1
    return -1

# Functions to get an array of rows, columns or boxes from the whole grid

def getRows(linearGrid):
    rows = [[], [], [], [], [], [], [], [], []]
    for square in range(81):
        rows[getRowIndex(square)].append(linearGrid[square])
    return rows

def getColumns(linearGrid):
    columns = [[], [], [], [], [], [], [], [], []]
    for square in range(81):
        columns[getColumnIndex(square)].append(linearGrid[square])
    return columns

def getBoxes(linearGrid):
    boxes = [[], [], [], [], [], [], [], [], []]
    for square in range(81):
        boxes[getBoxIndex(square)].append(linearGrid[square])
    return boxes