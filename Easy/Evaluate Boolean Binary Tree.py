from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluateTree(root: Optional[TreeNode]) -> bool:
    if root.left == None and root.right == None:
        if root.val == 0:
            return False
        if root.val == 1:
            return True
    left_result = evaluateTree(root.left)
    right_result = evaluateTree(root.right)
    if root.val == 2:
        return left_result or right_result
    return left_result and right_result