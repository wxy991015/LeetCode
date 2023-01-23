from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def equalToDescendants(root: Optional[TreeNode]) -> int:
    nodes = 0
    def descendantsSum(root: Optional[TreeNode]) -> int:
        ds = 0
        if not root:
            return 0
        if root.left:
            ds += root.left.val
            ds += descendantsSum(root.left)
        if root.right:
            ds += root.right.val
            ds += descendantsSum(root.right)
        return ds
    if not root:
        return 0
    stk = [root]
    while stk:
        node = stk.pop()
        ds = descendantsSum(node)
        if ds == node.val:
            nodes += 1
        if node.left:
            stk.append(node.left)
            ds = descendantsSum(node.left)
            if ds == node.left.val:
                nodes += 1
        if node.right:
            stk.append(node.right)
            ds = descendantsSum(node.right)
            if ds == node.right.val:
                nodes += 1
    return nodes