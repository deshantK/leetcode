import copy
def solve(grid, row, col, color, match, act):
    print ("Hi", row, col)
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return True
    if act[row][col] != match:
        if act[row][col] == -1:
            return False
        return True
    
    act[row][col] = -1
    check = solve(grid, row+1, col, color, match, act)
    check = solve(grid, row-1, col, color, match, act) or check
    check = solve(grid, row, col+1, color, match, act) or check
    check = solve(grid, row, col-1, color, match, act) or check
    #act[row][col] = match
    if check:
        grid[row][col] = color

    return False

        

grid = [[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]
act = copy.deepcopy(grid)

row = 0
col = 0
color = 3

solve(grid, row, col, color, grid[row][col], act)
print( grid)
        