class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# version 1 - recursion
def sumEvenGrandparent(root: TreeNode) -> int:
    sum_of_values = 0
    if not root:
        return 0
    if root.val % 2 == 0:
        if root.left and root.left.left:
            sum_of_values += root.left.left.val
        if root.left and root.left.right:
            sum_of_values += root.left.right.val
        if root.right and root.right.left:
            sum_of_values += root.right.left.val
        if root.right and root.right.right:
            sum_of_values += root.right.right.val
    sum_of_values += sumEvenGrandparent(root.left)
    sum_of_values += sumEvenGrandparent(root.right)
    return sum_of_values