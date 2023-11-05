# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find(lst, start, end, num):
    for index in range(start, end+1):
        if num == lst[index]:
            return index


def solve(preorder, p_index, inorder, left, right):
    if left > right:
        return None, p_index-1
    if p_index >= len(preorder):
        return None, p_index-1
    node = TreeNode(preorder[p_index])
    index = find(inorder, left, right, preorder[p_index])
    #print (node,left, right, p_index, index)
    #p_index+=1

    node.left, p_index = solve(preorder, p_index+1, inorder, left, index-1)

    #p_index +=1
    node.right, p_index = solve(preorder, p_index+1, inorder, index+1, right)
    return node, p_index


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
node, _ = solve(preorder, 0, inorder, 0, len(inorder)-1)
print ( node)

        