def solve(q, ans, move):
    while not q:
        return
    temp_q = []
    temp_ans = []
    while q:
        node = q.pop(0)
        temp_ans.append(node.val)
        if node.left:
            temp_q.append(node.left)
        if node.right:
            temp_q.append(node.right)
    if move:
        temp_ans.reverse()
    ans.append(temp_ans)
    solve(temp_q, ans, not move)
    return

root = None(InputTree)
ans = []
stack = []
if not root:
    print(ans)
stack.append(root)
solve(stack, ans, False)
print(ans)