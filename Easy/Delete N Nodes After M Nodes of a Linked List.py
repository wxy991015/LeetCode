class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1
def deleteNodes(head: ListNode, m: int, n: int) -> ListNode:
    p = ListNode()
    modified_list = p
    first_m, next_n = 0, 0
    while head:
        if first_m != m:
            p.next = ListNode(head.val)
            first_m += 1
        else:
            while next_n != n and head.next:
                head = head.next
                next_n += 1
            # make sure that the loop stops because of next_n == n instead of head.next == None
            if next_n == n:
                p.next = ListNode(head.val)
            first_m, next_n = 1, 0
        p = p.next
        head = head.next
    modified_list = modified_list.next
    return modified_list

# version 2 - Faster
# modify the original linked list instead of creating a new list
def deleteNodes(head: ListNode, m: int, n: int) -> ListNode:
    # define a new linked list p which adds a prev for head
    # p.val = 0, p.next = head
    p = ListNode(0, head)
    first_m = 0
    while head:
        if first_m < m - 1:
            first_m += 1
        else:
            next_n = 0
            while next_n < n and head.next:
                # delete node one by one
                # 1 -> 2 -> 3 -> 4 ==> 1.next = 1.next.next = 3 ==> ListNode(2) get deleted
                head.next = head.next.next
                next_n += 1
            first_m = 0
        head = head.next
    p = p.next
    return p