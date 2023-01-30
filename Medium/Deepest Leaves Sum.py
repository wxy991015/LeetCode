from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# version 1 - recursion
def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    deepest_leaves_sum = 0
    def maxDepth(root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(maxDepth(root.left), maxDepth(root.right)) + 1
    def helper(root: Optional[TreeNode], depth: int):
        nonlocal deepest_leaves_sum
        if not root: return
        if depth == max_depth: deepest_leaves_sum += root.val
        helper(root.left, depth+1)
        helper(root.right, depth+1)
    max_depth = maxDepth(root)
    print(max_depth)
    helper(root, 1)
    return deepest_leaves_sum

# version 2 - iterative
def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    deepest_leaves_sum = 0
    depth = 0
    stk = [(root, depth)]
    while stk:
        node, current_depth = stk.pop()
        if not node.left and not node.right:
            if depth < current_depth:
                deepest_leaves_sum = node.val
                depth = current_depth
            elif depth == current_depth:
                deepest_leaves_sum += node.val
        else:
            if node.left:
                stk.append((node.left, current_depth+1))
            if node.right:
                stk.append((node.right, current_depth+1))
    return deepest_leaves_sum