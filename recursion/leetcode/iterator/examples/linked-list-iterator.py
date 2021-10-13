from util import build


class LinkedListIterator:

    def __init__(self, head):
        self.curr = head

    def next(self):
        res = self.curr.val
        self.curr = self.curr.next
        return res

    def hasNext(self):
        return self.curr is not None


lli = LinkedListIterator(build([4, 5, 7, 8, 9]))
while lli.hasNext():
    print(lli.next())
