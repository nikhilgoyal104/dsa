from linked.util import cyclic


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
def _getCycleStart(head, meeting):
    start = head
    while start != meeting:
        start = start.next
        meeting = meeting.next
    return start


# T=n,S=1
def getCycleStart(head):
    meeting = getMeetingPoint(head)
    if not meeting:
        return None
    return _getCycleStart(head, meeting)


for nums, pos in [
    ([], -1),
    ([3, 2, 0, -4], 1),
    ([1, 2], 0),
    ([1], -1),
    ([1], 0),
    ([1, 3, 4], 1),
    ([1, 8, 3, 4], -1),
    ([1, 2, 3, 4, 5, 6, 7, 8], 2)
]:
    head = cyclic(nums, pos)
    start = getCycleStart(head)
    print(f'start val {start.val}' if start else 'no cycle')
    print(f'tail connects to node index pos {pos}' if pos != -1 else 'no cycle')