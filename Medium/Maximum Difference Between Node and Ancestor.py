from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    def dfs(root: Optional[TreeNode], max_val: int, min_val: int):
        nonlocal res
        res = max(abs(root.val-max_val), abs(root.val-min_val), res)
        max_val = max(max_val, root.val)
        min_val = min(min_val, root.val)
        if root.left:
            dfs(root.left, max_val, min_val)
        if root.right:
            dfs(root.right, max_val, min_val)
    res = 0
    max_val = min_val = root.val
    dfs(root, max_val, min_val)
    return res
        

root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right = TreeNode(10)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)
print(f"Output: {maxAncestorDiff(root)}")