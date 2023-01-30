from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def findLeaves(root: Optional[TreeNode]) -> List[List[int]]:
    leaves_nodes, temp = [], []
    def helper(root: Optional[TreeNode], temp: List[int], leaves_nodes: List[List[int]]) -> None:
        if not root: return
        if not root.left and not root.right:
            temp.append(root.val)
            del root
        helper(root.left, temp, leaves_nodes)
        helper(root.right, temp, leaves_nodes)
        leaves_nodes.append(temp)
        temp = []
    helper(root, temp, leaves_nodes)
    return leaves_nodes