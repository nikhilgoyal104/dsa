from util import b, ListNode


# T=n,S=1
def x(head, k):
    if not head:
        return head
    tail, n = head, 1
    while tail.next:
        n, tail = n + 1, tail.next
    tail.next, k = head, k % n
    for i in range(n - k):
        tail = tail.next
    res, tail.next = tail.next, None
    return res


for head, k in [
    (b([1, 2, 3, 4, 5]), 2),
    (b([0, 1, 2]), 4),
    (b([1]), 3),
    (b([]), 0)
]:
    print(x(head, k), end=' ')
