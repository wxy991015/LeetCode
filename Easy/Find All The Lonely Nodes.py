from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# version 1 - recursion
def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    def solver(root: Optional[TreeNode], result: List[int]) -> None:
        if not root:
            return
        if root.left and not root.right:
            result.append(root.left.val)
        elif root.right and not root.left:
            result.append(root.right.val)
        solver(root.left, result)
        solver(root.right, result)
    solver(root, result)
    return result

# version 2 - iteration
def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
    stk = [root]
    result = []
    while stk:
        node = stk.pop()
        if node.left:
            stk.append(node.left)
            if not node.right:
                result.append(node.left.val)
        if node.right:
            stk.append(node.right)
            if not node.left:
                result.append(node.right.val)
    return result

"""
def getLonelyNodes(self, root: TreeNode) -> List[int]:
        stk = [root]
        res = []
        
        while stk:
            node = stk.pop()
            
            if node.left:
                stk.append(node.left)
                
                if not node.right:
                    res.append(node.left.val)
                    
            if node.right:
                stk.append(node.right)
                
                if not node.left:
                    res.append(node.right.val)
        
        return res
"""