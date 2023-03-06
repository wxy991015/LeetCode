from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestValue(root: Optional[TreeNode], target: float) -> int:
    res = root.val
    currDiff = abs(root.val - target)
    def helper(root: Optional[TreeNode], target: float) -> int:
        nonlocal res, currDiff
        if root:
            if abs(root.val - target) < currDiff:
                currDiff = abs(root.val - target)
                res = root.val
            helper(root.left, target)
            helper(root.right, target)
    helper(root, target)
    return res

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
target = 3.714286
print(f"Output: {closestValue(root, target)}")