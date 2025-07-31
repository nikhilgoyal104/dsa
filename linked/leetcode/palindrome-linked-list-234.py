from zmq.backend import first

from linked.util import build, ListNode

inputs = [
    build([1, 2, 2, 1]),
    build([1, 2]),
    build([1, 2, 3, 2, 1]),
    build([1]),
    build([1, 2, 3]),
]


# T=n,S=n
def main(head):
    nums = []
    temp = head
    while temp:
        nums.append(temp.val)
        temp = temp.next
    return nums == nums[::-1]


for head in inputs:
    print(main(head))

print()


def reverse(head):
    prev = None
    curr = head
    while curr:
        _next = curr.next
        curr.next = prev
        prev = curr
        curr = _next
    return prev


def findMiddleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# T=n,S=1
def main(head):
    middle = findMiddleNode(head)
    first = head
    second = reverse(middle)
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True


for head in inputs:
    print(main(head))

print()
