from linked.util import build, ListNode


# T=n,S=1
def main(head, k):
    if not head:
        return head
    tail = head
    n = 1
    while tail.next:
        n += 1
        tail = tail.next
    tail.next = head
    k %= n
    for i in range(n - k):
        tail = tail.next
    res = tail.next
    tail.next = None
    return res


for head, k in [
    (build([1, 2, 3, 4, 5]), 2),
    (build([0, 1, 2]), 4),
    (build([1]), 3),
    (build([]), 0)
]:
    print(main(head, k), end=' ')
