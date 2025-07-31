class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        temp = self
        nums = []
        while temp:
            nums.append(temp.val)
            temp = temp.next
        return str(nums)


def add(head, val):
    if not head:
        return ListNode(val)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = ListNode(val)
    return head


def build(nums):
    head = None
    for val in nums:
        head = add(head, val)
    return head if head else []


def getNode(head, pos):
    temp = head
    while pos:
        temp = temp.next
        pos -= 1
    return temp


def getTail(head):
    temp = head
    while temp.next:
        temp = temp.next
    return temp


def getNodeAtVal(head, val):
    temp = head
    while temp:
        if temp.val == val:
            return temp
        temp = temp.next
    return None


def cyclic(nums, pos):
    head = build(nums)
    if pos == -1:
        return head
    node = getNode(head, pos)
    tail = getTail(head)
    tail.next = node
    return head


def intersected(intersectVal, listA, listB, skipA, skipB):
    if not intersectVal:
        return build(listA), build(listB)
    headA = build(listA)
    headB = build(listB[:skipB])
    getTail(headB).next = getNodeAtVal(headA, intersectVal)
    return headA, headB
