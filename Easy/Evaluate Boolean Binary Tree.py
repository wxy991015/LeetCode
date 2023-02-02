from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluateTree(root: Optional[TreeNode]) -> bool:
    evalution_result = False
    if root.left == None and root.right == None:
        if root.val == 0:
            return False
        if root.val == 1:
            return True
    if root.val == 2:
        if root.left.val == 0 and root.right.val == 0:
            pass
    return evalution_result