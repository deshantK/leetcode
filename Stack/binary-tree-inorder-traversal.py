def solve(node, ans):
    if not node:
        return
    solve(node.left, ans)
    ans.append(node.val)
    solve(node.right, ans)


class Solution(object):
    def inorderTraversal(self, root):
        ans = []
        solve(root, ans)
        return ans