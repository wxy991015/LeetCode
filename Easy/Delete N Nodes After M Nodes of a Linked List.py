class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNodes(head: ListNode, m: int, n: int) -> ListNode:
    head_copy = head
    p = head_copy
    m_count, n_count = 1, 0
    while head_copy:
        if m_count != m:
            m_count += 1
            head_copy = head_copy.next
            p = p.next
        else:
            while n_count != n:
                n_count += 1
                head_copy = head_copy.next
            p.next = head_copy.next
    return head

