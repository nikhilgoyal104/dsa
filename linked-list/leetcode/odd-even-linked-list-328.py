from util import b, ListNode


# T=n,S=1
def x(head):
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
    b([1, 2, 3, 4, 5]),
    b([2, 1, 3, 5, 6, 4, 7]),
    b([1, 2, 3, 4]),
    b([1, 2, 3, 4, 5, 6, 7, 8]),
    b([]),
    b([1, 2]),
    b([1, 2, 3])
]:
    print(x(head))
