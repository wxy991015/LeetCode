from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructFromPrePost(preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def constructTree(start: int, end: int, postorder: List[int], p_index: int, items: dict):
        if start > end:
            return None
        root = TreeNode(postorder[p_index-1])
        index = items[root.val]
        root.right = constructTree(index+1, end, postorder, p_index, items)
        root.left = constructTree(start, index, postorder, p_index, items)
        return root
    size = len(preorder)
    items = dict()
    for i in range(size):
        items[preorder[i]] = i
    p_index = size - 1
    return constructTree(0, size-1, postorder, p_index, items)