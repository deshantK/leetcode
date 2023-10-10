def search(word, row, col, grid):
  if len(word) == 0:
    return True
  if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
    return False
  if word[0] != grid[row][col]:
    return False
  grid[row][col] = '*' """Marking such that in next recursion this is not 
  scan second time. At last put actual charecter in this cell"""
  check = search(word[1:len(word)], row+1, col, grid)
  check = check or search(word[1:len(word)], row-1, col, grid)
  check = check or search(word[1:len(word)], row, col+1, grid)
  check = check or search(word[1:len(word)], row, col-1, grid)
  grid[row][col] = word[0]
  return check


grid = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
word = "eat"

for i in range(len(grid)):
   for j in range(len(grid[0])):
      if search(word, i, j, grid):
        print ("found")


