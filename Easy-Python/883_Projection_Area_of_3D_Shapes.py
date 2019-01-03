grid = [[1,1,1],
        [1,0,1],
        [1,1,1]]
# yz： max column
# xz:  max row
# xy: not 0


def projectionArea(grid):
    sum = 0
    for i in range(len(grid)): #row
        max_row = 0
        max_column = 0
        for j in range(len(grid)): # column

            if grid[i][j] != 0:
                sum += 1
            max_row = max(max_row, grid[i][j])
            max_column = max(max_column,grid[j][i])

        sum += max_column + max_row
    return sum