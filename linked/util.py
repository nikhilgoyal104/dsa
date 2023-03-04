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
