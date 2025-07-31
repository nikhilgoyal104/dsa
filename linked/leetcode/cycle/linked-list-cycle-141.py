from linked.util import cyclic

inputs = [
    cyclic([], -1),
    cyclic([3, 2, 0, -4], 1),
    cyclic([1, 2], 0),
    cyclic([1], -1),
    cyclic([1], 0),
    cyclic([1, 3, 4], 1),
    cyclic([1, 8, 3, 4], -1),
    cyclic([1, 2, 3, 4, 5, 6, 7, 8], 2)
]


# T=n,S=n
def main(head):
    seen = set()
    node = head
    while node:
        if node in seen:
            return True
        seen.add(node)
        node = node.next
    return False


for head in inputs:
    print(main(head))

print()


# T=n,S=1
def main(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


for head in inputs:
    print(main(head))

print()
