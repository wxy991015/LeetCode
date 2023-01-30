class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def balanceBST(root: TreeNode) -> TreeNode:
    if not root.left and not root.right:
        return root
    result = TreeNode(root.val)
    result_left, result_right = result.left, result.right
    def helper(root: TreeNode) -> None:
        nonlocal result, result_left, result_right
        if not root: return
        if not result_left:
            result_left = TreeNode(root.val)
            result_left = result_left.left
        if not result_right:
            result_right = TreeNode(root.val)
            result_right = result_right.right
        helper(root.left)
        helper(root.right)
    return result
        