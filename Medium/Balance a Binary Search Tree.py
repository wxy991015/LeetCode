from typing import List
import bisect

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# version 1 - brutal force
# use post order traversal for binary search tree
def balanceBST(root: TreeNode) -> TreeNode:
    pass