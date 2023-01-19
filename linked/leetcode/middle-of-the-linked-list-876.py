from linked.util import build, ListNode

inputs = [
    build([1, 2, 3, 4, 5]),
    build([1, 2, 3, 4, 5, 6])
]


# T=n,S=1
def main(head):
    count = 0
    temp = middle = head
    while temp:
        if count % 2:
            middle = middle.next
        count += 1
        temp = temp.next
    return middle


for head in inputs:
    print(main(head))

print()


# T=n,S=1
def main(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


for head in inputs:
    print(main(head))
