def solve(grid, row, col):
    n = len(grid)
    m = len(grid[0])
    if row < 0 or col < 0 or row >= n or col >= m:
        return 
    if grid[row][col] != "1":
        return
    grid[row][col] = "*"
    solve(grid, row+1, col)
    solve(grid, row-1, col)
    solve(grid, row, col+1)
    solve(grid, row, col-1)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
row = len(grid)
col = len(grid[0])
ans = 0
for i in range(row):
    for j in range(col):
        if grid[i][j] == "1":
            #print ("Hi")
            ans +=1
            solve(grid, i, j)
            print (grid)
print(ans)