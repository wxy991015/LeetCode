class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# version 1 - Recursive Approach
def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    if not original or target == original:
        return cloned
    return getTargetCopy(original.left, cloned.left, target) or getTargetCopy(original.right, cloned.right, target)

# version 2 - Iterative Approach
def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    current1 = original
    current2 = cloned
    found = None
    while current1:
        if not current1.left:
            if current1.val == target.val:
                found = current2
            current1 = current1.right
            current2 = current2.right
        else:
            temp1, temp2 = current1.left, current2.left
            while temp1.right and temp1.right != current1:
                temp1 = temp1.right
                temp2 = temp2.right
            if temp1.right == current1:
                temp1.right = None
                temp2.right = None
                if current1 == target:
                    found = current2
                current1 = current1.right
                current2 = current2.right
            else:
                temp1.right = current1
                temp2.right = current2
                current1 = current1.left
                current2 = current2.left
    return found