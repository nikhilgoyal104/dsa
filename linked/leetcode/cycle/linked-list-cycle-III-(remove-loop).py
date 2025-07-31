from linked.util import cyclic

inputs = [
    cyclic([], -1),
    cyclic([3, 2, 0, -4], 1),
    cyclic([1, 2], 0),
    cyclic([1], -1),
    cyclic([1], 0),
    cyclic([1, 3, 4], 1),
    cyclic([1, 8, 3, 4], -1),
    cyclic([1, 2, 3, 4, 5, 6, 7, 8], 2)
]


# T=n,S=1
def getMeetingPoint(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None


# T=n,S=1
def getCycleStart(head, meeting):
    start = head
    while start != meeting:
        start = start.next
        meeting = meeting.next
    return start


# T=n,S=1
def removeCycle(head):
    meeting = getMeetingPoint(head)
    if not meeting:
        return head
    prev = start = getCycleStart(head, meeting)
    while prev.next != start:
        prev = prev.next
    prev.next = None
    return head


for head in inputs:
    print(removeCycle(head))
