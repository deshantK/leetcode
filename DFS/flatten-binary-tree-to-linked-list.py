class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(self, root):
    if not root:
        return root
        
    cur = root
    while cur:
        if cur.left:
            next = cur.left
            while next.right:
                next = next.right
            next.right = cur.right
            cur.right = cur.left
            cur.left = None
        cur = cur.right
    return root



