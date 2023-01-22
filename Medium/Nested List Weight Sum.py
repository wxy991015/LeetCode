from typing import List, Deque

class NestedInteger:
    def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """
       
    def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       
    def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

    def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

    def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

    def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

# version 1 - backtrack
def depthSum(nestedList: List[NestedInteger]) -> int:
    def solver(nestedList: List[NestedInteger], depth: int) -> int:
        depth_sum = 0
        for i in range(len(nestedList)):
            nested_integer = nestedList[i]
            if nested_integer.isInteger():
                depth_sum += nested_integer.getInteger() * depth
            else:
                depth_sum += solver(nested_integer.getList(), depth+1)
        return depth_sum
    depth = 1
    depth_sum = solver(nestedList, depth)
    return depth_sum

# version 2 - breadth-first search (use deque)
def depthSum(nestedList: List[NestedInteger]) -> int:
    queue = Deque(nestedList)
    depth = 1
    total = 0
    while len(queue) > 0:
        for i in range(len(queue)):
            nested = queue.pop()
            if nested.isInteger():
                total += nested.getInteger() * depth
            else:
                queue.extendleft(nested.getList())
        depth += 1
    return total