from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# version 1 - general recursion
def getAllElements(root1: TreeNode, root2: TreeNode) -> List[int]:
    root1_elements, root2_elements = [], []
    def helper(root: TreeNode, elements: List[int]) -> None:
        if not root:
            return
        elements.append(root.val)
        helper(root.left)
        helper(root.right)
    helper(root1, root1_elements)
    helper(root2, root2_elements)
    return sorted(root1_elements + root2_elements)

# version 2 - binary search
