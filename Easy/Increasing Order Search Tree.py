class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasingBST(root: TreeNode) -> TreeNode:
    result_root = None
    def helper(root: TreeNode):
        nonlocal result_root
        if root.left:
            helper(root.left)
        result_root = TreeNode(root.val)
        if root.right:
            pass