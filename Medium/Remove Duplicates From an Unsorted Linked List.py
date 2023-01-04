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
