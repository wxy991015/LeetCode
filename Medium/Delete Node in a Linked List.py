class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# version 1 - Does not work (misunderstand the instructions)
def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    head = ListNode(0)
    result = head
    while head:
        if head.next.val == node.val:
            head.next = node.next
        head = head.next
    head = result.next

# version 2
def deleteNode1(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next