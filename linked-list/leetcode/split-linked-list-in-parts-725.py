from util import b


def size(head):
    size = 0
    while head:
        size, head = size + 1, head.next
    return size


# T=n+k,S=k
def x(head, k):
    res = []
    width, rem = divmod(size(head), k)
    i, prev, curr = 0, None, head
    while i < k and curr:
        res.append(curr)
        for _ in range(width - (0 if i < rem else 1)):
            curr = curr.next
        prev, curr = curr, curr.next
        prev.next = None
        i += 1
    return res if i == k else res + (k - i) * [None]


for head, k in [
    (b([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3),
    (b([1, 2, 3, 4, 5]), 5),
    (b([1, 2, 3, 4]), 5),
    (b([1, 2, 3]), 5),
]:
    print(x(head, k))
