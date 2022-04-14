def inputGrid():
    linearGrid = []
    print("Enter the sudoku as a single string of values with no spaces, commas or line breaks.")
    print("Use 0 for empty squares.")
    gridString = input()
    for i in gridString:
        linearGrid.append(int(i))
    return linearGrid

def outputGrid(linearGrid):
    for row in range(9):
        lineOutput = ""
        for square in range(9):
            lineOutput += str(linearGrid[(row * 9) + square])
        print(lineOutput)