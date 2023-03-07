from typing import List

def haveConflict(event1: List[str], event2: List[str]) -> bool:
    event1Start, event1End = event1[0], event1[1]
    event2Start, event2End = event2[0], event2[1]
    if event1Start > event2End or event2Start > event1End:
        return False
    return True

event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]
print(f"Output: {haveConflict(event1, event2)}")