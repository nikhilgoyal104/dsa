class Iterator:
    def __init__(self, nums):
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass


# T=1,S=1
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.curr = self.iterator.next()

    def next(self):
        res = self.curr
        self.curr = self.iterator.next() if self.iterator.hasNext() else None
        return res

    def hasNext(self):
        return self.curr is not None

    def peek(self):
        return self.curr


iter1 = PeekingIterator(Iterator(nums=[1, 2, 3]))


class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.top = None
        self.hasPeeked = False

    def peek(self):
        if not self.hasPeeked:
            self.hasPeeked = True
            self.top = self.iterator.next()
        return self.top

    def next(self):
        if not self.hasPeeked:
            return self.iterator.next()
        res = self.top
        self.top = None
        self.hasPeeked = False
        return res

    def hasNext(self):
        return self.hasPeeked or self.iterator.hasNext()


iter2 = PeekingIterator(Iterator(nums=[1, 2, 3]))
