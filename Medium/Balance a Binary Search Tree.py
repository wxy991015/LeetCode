class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def balanceBST(root: TreeNode) -> TreeNode:
    if root.left == None and root.right == None:
        return root
    result = TreeNode(root.val)
    if root.left:
        if result.left == None:
            result.left = TreeNode(root.left.val)
            result = result.left
    else:
        if result.left:
            pass
    return result
        