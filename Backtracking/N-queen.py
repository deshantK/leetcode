#checking whether current position of queen is current or not
def is_valid(cur_row, cur_col, sol):   
  for i in range(cur_row):
    old_row = i
    old_col = sol[i]
    if old_col == cur_col or abs(old_row-cur_row) == abs(old_col - cur_col):
      return False
  return True


def solve(n, row, sol, result):
  print (n, row)
  if row == n:
    result.append(sol)
    return
  for i in range(0, n):
    check = is_valid(row, i, sol)
    print (i, check)
    if check:
      sol[row] = i
      solve(n, row+1, sol, result)
  return

n = 4
sol = [-1]*n
result = []
solve(n, 0, sol, result)
print (result)
