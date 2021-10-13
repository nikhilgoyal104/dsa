class Vector2D:

    def __init__(self, vec):
        self.pos = 0
        self.nums = [val for sublist in vec for val in sublist]

    def next(self):
        res = self.nums[self.pos]
        self.pos += 1
        return res

    def hasNext(self):
        return self.pos < len(self.nums)


vector = Vector2D([[]])
print(vector.hasNext())


class Vector2D:

    def __init__(self, vec):
        self.inner = self.outer = 0
        self.vec = vec

    def skipEmptyLists(self):
        while self.outer < len(self.vec) and self.vec[self.outer] == []:
            self.outer += 1

    def next(self):
        self.skipEmptyLists()
        res = self.vec[self.outer][self.inner]
        self.inner += 1
        if self.inner == len(self.vec[self.outer]):
            self.outer += 1
            self.inner = 0
        return res

    def hasNext(self):
        self.skipEmptyLists()
        return self.outer < len(self.vec)


vector = Vector2D([[]])
print(vector.hasNext())
