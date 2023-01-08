class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1 - time limit exceeded
def deleteDuplicatesUnsorted(head: ListNode) -> ListNode:
    p = ListNode()
    deleted_linked_list = p
    deleted_duplicates = []
    while head:
        deleted_duplicates.append(head.val)
        head = head.next
    for i in deleted_duplicates:
        if deleted_duplicates.count(i) > 1:
            deleted_duplicates = [val for val in deleted_duplicates if val != i]
    for i in deleted_duplicates:
        p.next = ListNode(i)
        p = p.next
    return deleted_linked_list.next

# version 2
def deleteDuplicatesUnsorted1(head: ListNode) -> ListNode:
    cnt = dict()
    cur = head
    while cur:
        cnt[cur.val] = cnt.get(cur.val, 0) + 1
        cur = cur.next
    aux = {k for k, v in cnt.items() if v > 1}
    dummy = ListNode(0)
    prev = dummy
    cur = head
    while cur:
        while cur and cur.val in aux:
            cur = cur.next
        prev.next = cur
        if cur:
            prev = cur
            cur = cur.next
    return dummy.next