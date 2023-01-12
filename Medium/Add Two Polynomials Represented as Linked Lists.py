class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next

def addPoly(poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
    p = PolyNode()
    result = p
    while poly1 and poly2:
        if poly1.power == poly2.power:
            coefficient = poly1.coefficient + poly2.coefficient
            power = poly1.power
            if coefficient != 0:
                p.next = PolyNode(coefficient, power)
                p = p.next
            poly1 = poly1.next
            poly2 = poly2.next
        elif poly1.power > poly2.power:
            coefficient = poly1.coefficient
            power = poly1.power
            if coefficient != 0:
                p.next = PolyNode(coefficient, power)
                p = p.next
            poly1 = poly1.next
        else:
            coefficient = poly2.coefficient
            power = poly2.power
            if coefficient != 0:
                p.next = PolyNode(coefficient, power)
                p = p.next
            poly2 = poly2.next
    if poly1:
        while poly1:
            coefficient = poly1.coefficient
            power = poly1.power
            if coefficient != 0:
                p.next = PolyNode(coefficient, power)
                p = p.next
            poly1 = poly1.next
    if poly2:
        while poly2:
            coefficient = poly2.coefficient
            power = poly2.power
            if coefficient != 0:
                p.next = PolyNode(coefficient, power)
                p = p.next
            poly2 = poly2.next  
    return result.next