class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# version 1
def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    start = list1
    count = 1
    # get the start of removing
    while count != a:
        count += 1
        start = start.next
    
    # get the end of removing
    end = start.next
    while count != b:
        count += 1
        end = end.next
    
    # insert list2 between start and end
    while list2:
        start.next = list2
        list2 = list2.next
        start = start.next
    start.next = end.next
    return list1

# version 2
def mergeInBetween1(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    curr=list1
    t=0
    var=None
    while curr!=None:
        t+=1
        if t==b+1:
            break
        if a==t:
            pp=curr.next
            var=curr
            var.next=list2
            # curr.next=None
            curr=pp
        curr=curr.next
    temp=list1
    while temp!=None:
        if temp.next==None:
            break
        temp=temp.next
    temp.next=curr
    return list1