from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1
def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if left == right:
        return head
    result = ListNode(0)
    p = result
    nodes = []
    while head:
        nodes.append(head.val)
        head = head.next
    nodes[left-1:right] = nodes[left-1:right][::-1]
    for i in nodes:
        p.next = ListNode(i)
        p = p.next
    return result.next

# version 2 - recursion
def reverseBetween(head, m, n):
    if not head:
        return None
    left, right = head, head
    stop = False
    def recurseAndReverse(right, m, n):
        nonlocal left, stop
        # base case. Don't proceed any further
        if n == 1:
            return
        # Keep moving the right pointer one step forward until (n == 1)
        right = right.next
        # Keep moving left pointer to the right until we reach the proper node
        # from where the reversal is to start.
        if m > 1:
            left = left.next
        # Recurse with m and n reduced.
        recurseAndReverse(right, m - 1, n - 1)
        # In case both the pointers cross each other or become equal, we
        # stop i.e. don't swap data any further. We are done reversing at this
        # point.
        if left == right or right.next == left:
            stop = True
        # Until the boolean stop is false, swap data between the two pointers
        if not stop:
            left.val, right.val = right.val, left.val
            # Move left one step to the right.
            # The right pointer moves one step back via backtracking.
            left = left.next
    recurseAndReverse(right, m, n)
    return head