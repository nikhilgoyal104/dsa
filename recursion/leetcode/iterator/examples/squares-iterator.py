class SquaresIterator:

    def __init__(self):
        self.curr = 0

    def next(self):
        res = self.curr ** 2
        self.curr += 1
        return res


squaresIter = SquaresIterator()
for i in range(6):
    print(squaresIter.next())
