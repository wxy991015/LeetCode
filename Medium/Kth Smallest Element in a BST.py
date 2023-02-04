from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# version 1 - simple inorder
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    nodes_collections = []
    def inorder(root: Optional[TreeNode], nodes_collections: List[int]) -> None:
        if root:
            inorder(root.left, nodes_collections)
            nodes_collections.append(root.val)
            inorder(root.right, nodes_collections)
    inorder(root, nodes_collections)
    return nodes_collections[k-1]

# version 2 - iterative
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    n = 0
    stack = []
    current = root
    while current and stack:
        while current:
            stack.append(current)
            current = current.left
        stack.pop()
        current = stack.pop()
        n += 1
        if n == k:
            return current.val
        current = current.right
    return