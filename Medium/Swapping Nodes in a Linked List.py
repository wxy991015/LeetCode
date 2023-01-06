from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1
def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    size = 0
    p, end, swap_result = head, head, head
    while head:
        size += 1
        head = head.next
    beginning_k, end_k = k, size - k
    i, j = 1, 0
    head = p
    while i != beginning_k:
        head = head.next
    while j != end_k:
        end = end.next
    temp = head.val
    head.val = end.val
    end.val = temp
    return swap_result

# version 2 - Faster
def swapNodes1(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    temp=head
    c=1
    while temp.next!=None:
        if c==k:
            temp2=temp
        temp=temp.next
        c+=1

    # return if k equals to the length of head
    if c==k:
        temp.val,head.val=head.val,temp.val
        print("Hello")
        return head
    c,c2=c-k+1,1
    temp=head
    
    # return otherwise
    while c2!=c:
        temp=temp.next
        c2+=1
    temp.val,temp2.val=temp2.val,temp.val
    return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
k = 4
print(f"Output: {swapNodes1(head, k)}")