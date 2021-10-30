from linked.util import build


# T=n,S=1
def main(head):
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev


for head in [
    build([1]),
    build([1, 2, 3, 4, 5]),
    build([1, 2])
]:
    print(main(head))

print()


# T=n,S=n
def main(head):
    def rec(head):
        if not head or not head.next:
            return head
        last = rec(head.next)
        head.next.next, head.next = head, None
        return last

    return rec(head)


for head in [
    build([1]),
    build([1, 2]),
    build([1, 2, 3, 4, 5]),
]:
    print(main(head))
