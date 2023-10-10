def set_dp(dp, set_, area):
    for pair in set_:
        dp[pair[0]][pair[1]] = area


def solve(grid, row, col, set_):
    n = len(grid)
    m = len(grid[0])
    if row < 0 or col < 0 or row >= n or col >= m:
        return 0
    if grid[row][col] != 1:
        return 0
    if (row,col) in set_:
        return 0
    ans = 1
    set_.add((row, col))
    ans += solve(grid, row+1, col, set_)
    ans += solve(grid, row-1, col, set_)
    ans += solve(grid, row, col+1, set_)
    ans += solve(grid, row, col-1, set_)
    return ans


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

rows = len(grid)
colms = len(grid[0])
dp = [[-1 for i in range(colms) ] for j in range(rows)]
ans = 0
for i in range(rows):
    for j in range(colms):
        if grid[i][j] == 1:
            if dp[i][j] > 0:
                ans = max(ans, dp[i][j])
            else:
                set_ = set()
                area = solve(grid, i, j, set_)
                ans = max(ans, area)
                set_dp(dp,set_, area)
print (ans)