class Iterator:
    def __init__(self, nums):
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        self.iterator = iterator
        self.peeked = self.iterator.next()

    def peek(self):
        return self.peeked

    def next(self):
        res = self.peeked
        self.peeked = self.iterator.next() if self.iterator.hasNext() else None
        return res

    def hasNext(self):
        return self.peeked is not None


iter1 = PeekingIterator(Iterator(nums=[1, 2, 3]))


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        self.iterator = iterator
        self.peeked = None
        self.hasPeeked = False

    def peek(self):
        if not self.hasPeeked:
            self.hasPeeked = True
            self.peeked = self.iterator.next()
        return self.peeked

    def next(self):
        if not self.hasPeeked:
            return self.iterator.next()
        res = self.peeked
        self.peeked = None
        self.hasPeeked = False
        return res

    def hasNext(self):
        return self.hasPeeked or self.iterator.hasNext()


iter2 = PeekingIterator(Iterator(nums=[1, 2, 3]))
