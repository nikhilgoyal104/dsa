from heapq import *
from util import b, ListNode


# T=nklog(nk),S=nk
def x(lists):
    values = []
    for head in lists:
        while head:
            values.append(head.val)
            head = head.next
    dummy = tail = ListNode(-1)
    values.sort()
    for val in values:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next


for lists in [
    [b([1, 4, 5]), b([1, 3, 4]), b([2, 6])],
    [b([2, 6, 8]), b([3, 6, 7]), b([1, 3, 4])],
]:
    print(x(lists), end=' ')

print()


# T=nk²,S=1
def x(lists):
    def merge(h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1
        if h1.val < h2.val:
            h1.next = merge(h1.next, h2)
            return h1
        h2.next = merge(h1, h2.next)
        return h2

    merged = lists[0]
    for i in range(1, len(lists)):
        merged = merge(merged, lists[i])
    return merged


for lists in [
    [b([1, 4, 5]), b([1, 3, 4]), b([2, 6])],
    [b([2, 6, 8]), b([3, 6, 7]), b([1, 3, 4])],
]:
    print(x(lists), end=' ')

print()


# T=k+nklogk,S=k
def x(lists):
    heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
    heapify(heap)
    dummy = tail = ListNode(-1)
    while heap:
        val, i, head = heappop(heap)
        tail.next = head
        tail = tail.next
        if head.next:
            heappush(heap, (head.next.val, i, head.next))
    return dummy.next


for lists in [
    [b([1, 4, 5]), b([1, 3, 4]), b([2, 6])],
    [b([2, 6, 8]), b([3, 6, 7]), b([1, 3, 4])],
]:
    print(x(lists), end=' ')
