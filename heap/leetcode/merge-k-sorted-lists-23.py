from heapq import *
from util import b, ListNode


# T=Nlog(N),S=N
def main(lists):
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
    print(main(lists), end=' ')

print()


# T=Nk,S=1
def main(lists):
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
    print(main(lists), end=' ')

print()


# T=k+Nlogk,S=k
def main(lists):
    heap = []
    for i, head in enumerate(lists):
        if head:
            heap.append((head.val, i, head))
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
    print(main(lists), end=' ')
