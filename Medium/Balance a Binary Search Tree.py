from typing import List
import bisect

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# version 1 - brutal force
# use post order traversal to collect binary search tree
def balanceBST(root: TreeNode) -> TreeNode:
    nodes = []
    def post_order(root: TreeNode) -> None:
        if root:
            post_order(root.left)
            nodes.append(root.val)
            post_order(root.right)
    post_order(root)
    def buid_tree(nodes: List[int]):
        if not nodes:
            return
        mid = len(nodes) // 2
        result = TreeNode(nodes[mid])
        result.left = buid_tree(nodes[0:mid])
        result.right = buid_tree(nodes[mid+1:])
        return result
    return buid_tree(nodes)