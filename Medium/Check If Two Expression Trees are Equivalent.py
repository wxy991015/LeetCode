class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# version 1 - inorder traversal
def checkEquivalence(root1: 'Node', root2: 'Node') -> bool:
    def formula(root: 'Node') -> str:
        res = ""
        if not root:
            return ""
        res += formula(root.left) + root.val + formula(root.right)
        return res
    res1 = formula(root1)
    res2 = formula(root2)
    return sorted(res1) == sorted(res2)