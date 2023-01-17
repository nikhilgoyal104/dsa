from linked.util import build


# T=n,S=1
def main(head):
    prev, curr = None, head
    while curr:
        future = curr.next
        curr.next = prev
        prev = curr
        curr = future
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
    def dfs(head):
        if not head or not head.next:
            return head
        last = dfs(head.next)
        head.next.next = head
        head.next = None
        return last

    return dfs(head)


for head in [
    build([1]),
    build([1, 2]),
    build([1, 2, 3, 4, 5]),
]:
    print(main(head))
