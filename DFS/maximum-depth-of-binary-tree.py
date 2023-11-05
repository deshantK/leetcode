def solve(node):
    if not node:
        return 0
    return 1 + max(solve(node.left), solve(node.right))