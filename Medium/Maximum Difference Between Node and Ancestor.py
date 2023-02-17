from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    nodes = []
    def nodesCollections(root: Optional[TreeNode], nodes: List[int]) -> None:
        if root:
            nodesCollections(root.left, nodes)
            nodes.append(root.val)
            nodesCollections(root.right, nodes)
    nodesCollections(root, nodes)
    print(nodes)
    root_val = root.val
    root_index = nodes.index(root_val)
    left_nodes = nodes[0:root_index+1]
    right_nodes = nodes[root_index:]
    left_max = max(left_nodes) - min(left_nodes)
    right_max = max(right_nodes) - min(right_nodes)
    return max(left_max, right_max)

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