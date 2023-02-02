from typing import List, Optional
import bisect

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
    root = TreeNode(preorder[0])
    index = 1
    def helper(root: TreeNode, index: int):
        nonlocal preorder
        if index == len(preorder):
            return
        if preorder[index] < root.val:
            root.left = TreeNode(preorder[index])
        else:
            root.right = TreeNode(preorder[index])
        root