from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# version 1 - recursive solution
def averageOfSubtree(root: Optional[TreeNode]) -> int:
    equal_to_average = 0
    def sumOfNodes(root: Optional[TreeNode]):
        sum_of_nodes = 0
        if not root:
            return 0
        sum_of_nodes += root.val
        sum_of_nodes += sumOfNodes(root.left)
        sum_of_nodes += sumOfNodes(root.right)
        return sum_of_nodes
    def numOfNodes(root: Optional[TreeNode]):
        num_of_nodes = 0
        if not root:
            return 0
        num_of_nodes += 1
        num_of_nodes += numOfNodes(root.left)
        num_of_nodes += numOfNodes(root.right)
        return num_of_nodes
    if not root:
        return 0
    if root.val == sumOfNodes(root) // numOfNodes(root):
        equal_to_average += 1
    equal_to_average += averageOfSubtree(root.left)
    equal_to_average += averageOfSubtree(root.right)
    return equal_to_average