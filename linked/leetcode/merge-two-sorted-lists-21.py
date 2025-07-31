from linked.util import build, ListNode


# T=m+n,S=m+n
def main(h1, h2):
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
    (build([1, 2, 4]), build([1, 3, 4])),
    (build([]), build([])),
    (build([1, 2, 3]), build([])),
    (build([1, 2, 3]), build([4, 5, 6])),
    (build([]), build([0])),
]:
    print(main(h1, h2))

print()


# T=m+n,S=m+n
def main(h1, h2):
    head = tail = ListNode(-1)
    while h1 and h2:
        if h1.val < h2.val:
            tail.next = ListNode(h1.val)
            h1 = h1.next
        else:
            tail.next = ListNode(h2.val)
            h2 = h2.next
        tail = tail.next
    while h1:
        tail.next = ListNode(h1.val)
        h1 = h1.next
        tail = tail.next
    while h2:
        tail.next = ListNode(h2.val)
        h2 = h2.next
        tail = tail.next
    return head.next


for h1, h2 in [
    (build([1, 2, 4]), build([1, 3, 4])),
    (build([]), build([])),
    (build([1, 2, 3]), build([])),
    (build([1, 2, 3]), build([4, 5, 6])),
    (build([]), build([0]))
]:
    print(main(h1, h2))

print()


# T=m+n,S=1
def main(h1, h2):
    head = tail = ListNode(-1)
    while h1 and h2:
        if h1.val < h2.val:
            tail.next = h1
            h1 = h1.next
        else:
            tail.next = h2
            h2 = h2.next
        tail = tail.next
    tail.next = h1 or h2
    return head.next


for h1, h2 in [
    (build([1, 2, 4]), build([1, 3, 4])),
    (build([]), build([])),
    (build([1, 2, 3]), build([])),
    (build([1, 2, 3]), build([4, 5, 6])),
    (build([]), build([0]))
]:
    print(main(h1, h2))
