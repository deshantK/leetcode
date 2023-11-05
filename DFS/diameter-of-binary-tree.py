# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def solve(root, dia):
    if not root:
        return dia, 0
    ldia, lh = solve(root.left, dia)
    rdia, rh = solve(root.right, dia)
    dia = max(lh+rh, dia, ldia, rdia)
    return dia, max(lh, rh)+1

class Solution(object):
    def diameterOfBinaryTree(self, root):
        dia = 0
        if not root:
            return 0
        dia, ht = solve(root, dia)
        return dia
