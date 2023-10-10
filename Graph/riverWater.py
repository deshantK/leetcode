def dfs(mat, visited, row, col):
    stack = []
    stack.append((row, col))
    rows, cols = len(mat), len(mat[0])
    while stack:
        row_, col_ = stack.pop()
        if (row_, col_) not in visited:
            visited.add((row_, col_))
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row = row_+x
                new_col = col_+y
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if mat[row_][col_] <= mat[new_row][new_col]:
                         stack.append((new_row, new_col))


heights = [[1,1],[1,1],[1,1]]
p_vis = set()
a_vis = set()
p_stack = []
a_stack = []
rows = len(heights)
cols = len(heights[0])
for r in range(rows):
    dfs(heights, p_vis, r, 0)
    dfs(heights, a_vis, r, cols-1)

for c in range(cols):
    dfs(heights, p_vis, 0, c)
    dfs(heights, a_vis, rows-1, c)
ans = p_vis.intersection(a_vis)
print( ans)