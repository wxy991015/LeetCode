from typing import List, Optional
import bisect

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    new_index = bisect.bisect(preorder, preorder[0])
    root.left = bstFromPreorder(preorder[1:new_index])
    root.right = bstFromPreorder(preorder[new_index:])
    return root