class NestedInteger:
    def isInteger(self):
        pass

    def getInteger(self):
        pass

    def getList(self):
        pass


# T=n+l,S=n+d
class NestedIterator:
    def __init__(self, nested):
        self.pos = 0
        self.nums = []

        def dfs(nested):
            for val in nested:
                if val.isInteger():
                    self.nums.append(val)
                    continue
                dfs(val.getList())

        dfs(nested)

    def next(self):
        res = self.nums[self.pos]
        self.pos += 1
        return res

    def hasNext(self):
        return self.pos < len(self.nums)


nestedIter = NestedIterator([])


# T=n+l,S=n+d
class NestedIterator:
    def __init__(self, nested):
        self.stack = list(reversed(nested))

    def next(self):
        self.makeTopAnInteger()
        return self.stack.pop()

    def hasNext(self):
        self.makeTopAnInteger()
        return len(self.stack) > 0

    def makeTopAnInteger(self):
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(list(reversed(self.stack.pop().getList())))
