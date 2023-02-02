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

# version 2 - faster recursive solution
def averageOfSubtree(root: Optional[TreeNode]) -> int:
    equal_to_average = 0
    def sumSizeOfNodes(root: Optional[TreeNode]):
        nonlocal equal_to_average
        if not root:
            return 0, 0
        left_sum, left_num = sumSizeOfNodes(root.left)
        right_sum, right_num = sumSizeOfNodes(root.right)
        nodes_sum = root.val + left_sum + right_sum
        nodes_num = 1 + left_num + right_num
        if nodes_sum // nodes_num == root.val:
            equal_to_average += 1
        return nodes_sum, nodes_num
    if not root:
        return 0
    sumSizeOfNodes(root)
    return equal_to_average