# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(root, ans):
    if not root:
        return ans, 0
    lans, leftval = solve(root.left, ans)
    rans, rightval = solve(root.right, ans)
    leftval = max(0, leftval)
    rightval = max(0, rightval)
    new_ans = leftval+rightval+root.val
    ans = max(new_ans, ans, lans, rans)
    path = root.val + max(leftval, rightval)
    return ans, path

        