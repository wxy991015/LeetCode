class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1
def plusOne(head: ListNode) -> ListNode:
    num = 0
    while head:
        num = num * 10 + head.val
        head = head.next
    num += 1
    temp = num
    digits = 0
    while temp:
        temp //= 10
        digits += 1
    start = 10 ** (digits - 1)
    p = ListNode(num//start)
    result = p
    if digits == 1:
        return result
    num %= start
    start //= 10
    while start >= 1:
        p.next = ListNode(num//start)
        num %= start
        start //= 10
        p = p.next
    return result