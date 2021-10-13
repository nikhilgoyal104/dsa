class RangeIterator:

    def __init__(self, min, max):
        self.curr = min
        self.max = max

    def next(self):
        res = self.curr
        self.curr += 1
        return res

    def hasNext(self):
        return self.curr < self.max


rangeIter = RangeIterator(12, 18)
while rangeIter.hasNext():
    print(rangeIter.next())
