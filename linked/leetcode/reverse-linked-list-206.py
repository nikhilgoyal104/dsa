from linked.util import build


# T=n,S=1
def main(head):
    prev = None
    curr = head
    while curr:
        _next = curr.next
        curr.next = prev
        prev = curr
        curr = _next
    return prev


for head in [
    build([]),
    build([1]),
    build([1, 2]),
    build([1, 2, 3, 4, 5])
]:
    print(main(head))


# T=n,S=n
def main(head):
    if not head:
        return None

    def dfs(head):
        if not head.next:
            return head
        last = dfs(head.next)
        head.next.next = head
        head.next = None
        return last

    return dfs(head)


for head in [
    build([]),
    build([1]),
    build([1, 2]),
    build([1, 2, 3, 4, 5]),
]:
    print(main(head))
