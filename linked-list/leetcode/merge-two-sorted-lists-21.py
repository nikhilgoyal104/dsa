from util import b, ListNode


# T=m+n,S=m+n
def x(h1, h2):
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

    return merge(h1, h2)


for h1, h2 in [
    (b([1, 2, 4]), b([1, 3, 4])),
    (b([]), b([])),
    (b([1, 2, 3]), b([]))
]:
    print(x(h1, h2))

print()


# T=m+n,S=1
def y(h1, h2):
    dummy = tail = ListNode(-1)
    while h1 and h2:
        if h1.val < h2.val:
            tail.next, h1 = h1, h1.next
        else:
            tail.next, h2 = h2, h2.next
        tail = tail.next
    tail.next = h1 or h2
    return dummy.next


for h1, h2 in [
    (b([1, 2, 4]), b([1, 3, 4])),
    (b([]), b([])),
    (b([1, 2, 3]), b([]))
]:
    print(y(h1, h2))
