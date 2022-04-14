from gridManipulation import getBoxes, getColumns, getRows

def isValid(linearGrid):
    if len(linearGrid) != 81:
        return False
    
    for i in linearGrid:
        if i > 9 or i < 0:
            return False
    
    boxes = getBoxes(linearGrid)
    for box in boxes:
        if hasDuplicates(box):
            return False
    
    rows = getRows(linearGrid)
    for row in rows:
        if hasDuplicates(row):
            return False

    columns = getColumns(linearGrid)
    for column in columns:
        if hasDuplicates(column):
            return False
    
    return True

def hasDuplicates(subGrid):
    for i in range(1,10):
        if subGrid.count(i) > 1:
            return True
    return False