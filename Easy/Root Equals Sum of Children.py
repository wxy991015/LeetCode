from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkTree(root: Optional[TreeNode]) -> bool:
    return root.left.val + root.right.val == root.val

root = [10,4,6]
print(f"Output: {checkTree(root)}")