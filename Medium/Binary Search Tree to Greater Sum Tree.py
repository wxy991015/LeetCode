class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# version 1: recursion
def bstToGst(root: TreeNode) -> TreeNode:
    
    def helper(root: TreeNode) -> int:
        if not root:
            return 0
        helper(root.right)
        