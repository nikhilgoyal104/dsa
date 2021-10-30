from linked.util import build, ListNode


# T=n,S=1
def main(head):
    if not head:
        return None
    oddHead = oddTail = head
    evenHead = evenTail = head.next
    while oddTail.next and evenTail.next:
        oddTail.next = oddTail.next.next
        oddTail = oddTail.next
        evenTail.next = evenTail.next.next
        evenTail = evenTail.next
    oddTail.next = evenHead
    return oddHead


for head in [
    build([1, 2, 3, 4, 5]),
    build([2, 1, 3, 5, 6, 4, 7]),
    build([1, 2, 3, 4]),
    build([1, 2, 3, 4, 5, 6, 7, 8]),
    build([]),
    build([1, 2]),
    build([1, 2, 3])
]:
    print(main(head))
