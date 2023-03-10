from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# version 1 - brute force
def increasingBST(root: TreeNode) -> TreeNode:
    if not root:
        return None
    nodes = []
    def nodes_collections(root: TreeNode, nodes: List[int]) -> None:
        if not root:
            return
        nodes.append(root.val)
        nodes_collections(root.left, nodes)
        nodes_collections(root.right, nodes)
    nodes_collections(root, nodes)
    nodes = sorted(nodes)
    p = TreeNode()
    result = p
    for i in nodes:
        p.right = TreeNode(i)
        p = p.right
    return result.right

# version 2 - inorder traversal
def increasingBST(root: TreeNode) -> TreeNode:
    def nodes_collections(root: TreeNode, nodes: List[int]) -> None:
        if not root:
            return
        nodes_collections(root.left, nodes)
        nodes.append(root)
        nodes_collections(root.right, nodes)
    if not root: return None
    nodes = []
    nodes_collections(root, nodes)
    for i in range(len(nodes)-1):
        nodes[i].right = nodes[i+1]
        nodes[i].left = None
    nodes[len(nodes)-1].left = None
    nodes[len(nodes)-1].right = None
    return nodes[0]