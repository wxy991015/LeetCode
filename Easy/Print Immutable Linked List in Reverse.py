class ImmutableListNode:
    def printValue(self) -> None: pass# print the value of this node.
    def getNext(self) -> 'ImmutableListNode': pass # return the next node.

# version 1 - Recursion
def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
    if head.getNext():
        self.printLinkedListInReverse(head.getNext())
    # why this instead of "else: head.printValue()"
    head.printValue()

# version 2 - Iteration
def printLinkedListInReverse1(self, head: 'ImmutableListNode') -> None:
    list_val = []
    while head:
        list_val.append(head)
        head = head.getNext()
    while list_val:
        list_val.pop().printValue()