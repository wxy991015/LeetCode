from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isUnivalTree(root: Optional[TreeNode]) -> bool:
    compare = root.val
    def helper(root: Optional[TreeNode], compare: int) -> bool:
        if not root:
            return True
        res = helper(root.left, compare) and helper(root.right, compare)
        if root.val != compare:
            return False
        return res
    return helper(root, compare)