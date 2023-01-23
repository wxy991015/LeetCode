from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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