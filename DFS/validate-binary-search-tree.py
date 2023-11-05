def solve(node):
    leftmin, leftmax, leftStatus = float('-inf'), float('-inf'), True
    rightmin, rightmax, rightStatus = float('inf'), float('inf'), True
    min_ = node.val
    max_ = node.val
    if node.left:
        leftmin, leftmax, leftStatus = solve(node.left)
        min_ = min(min_, leftmin)
        max_ = max(max_, leftmax)

    if node.right:
        rightmin, rightmax, rightStatus = solve(node.right)
        min_ = min(min_, rightmin)
        max_ = max(max_, rightmax)
    
    if leftmax < node.val and rightmin > node.val:
        return min_, max_, (True and leftStatus and rightStatus)
    return min_, max_, False