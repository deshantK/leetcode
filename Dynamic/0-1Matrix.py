def solve(matrix):
    rows = len(matrix)
    col = len(matrix[0])
    for i in range(rows):
        for j in range(col):
            if matrix[i][j] > 0:
                above = matrix[i - 1][j] if i > 0 else float('inf')
                left = matrix[i][j-1] if j > 0 else float('inf')
                matrix[i][j] = 1+min(above, left)
    for i in range(rows - 1, -1, -1):
        for j in range(col - 1, -1, -1):
            if matrix[i][j] > 0:
                right = matrix[i + 1][j] if i < rows-1 else float('inf')
                low = matrix[i][j+1] if j < col-1 else float('inf')    
                matrix[i][j] = min(right+1, low+1, matrix[i][j])

    

matrix =[[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
#matrix = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
row = len(matrix)
col = len(matrix[0])
dp = [[-1 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        solve(matrix)
print(matrix)