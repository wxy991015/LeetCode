from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
     
# version 1: recursion   
def rangeSumBST1(root: Optional[TreeNode], low: int, high: int) -> int:
    nodes_sum = 0
    if not root:
        return 0
    if root and low <= root.val <= high:
        nodes_sum += root.val
    nodes_sum += rangeSumBST1(root.left, low, high)
    nodes_sum += rangeSumBST1(root.right, low, high)
    return nodes_sum

# version 2: iteration
def rangeSumBST2(root: Optional[TreeNode], low: int, high: int) -> int:
    nodes_sum = 0
    