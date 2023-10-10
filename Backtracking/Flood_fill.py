def solve(grid, row, col, target, match):
    if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
        return
    if grid[row][col] != match:
        return
    
    grid[row][col] = "*"
    solve(grid, row+1, col, target, match)
    solve(grid, row-1, col, target, match)
    solve(grid, row, col+1, target, match)
    solve(grid, row, col-1, target, match)
    grid[row][col] = target


grid = [[1,1,0,0],[0,1,0,0],[0,1,1,0],[1,0,1,0]]
solve(grid, 2, 3, 0, grid[2][3])
print (grid)