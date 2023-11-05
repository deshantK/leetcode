# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def solve_ser(root, stack):
    if not root:
        stack.append("M")
        return
    stack.append(root.val)
    solve_ser(root.left, stack)
    solve_ser(root.right, stack)
    

def solve_des(stack):
    val = stack.pop()

    if type(val) is str and val == "M":
        return None

    node = TreeNode(val)

    node.left = solve_des(stream)
    node.right = solve_des(stream)

    return node



class Codec:

    def serialize(self, root):
        stack = []
        solve_ser(root, stack)
        print(stack)
        return stack
        

    def deserialize(self, data):
        print ("Desc")
        print (data)
        if len(data) == 0:
            return None
        data.reverse()
        root = solve_des(data)
        return root
