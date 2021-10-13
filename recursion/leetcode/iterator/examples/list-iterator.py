class Iterator:
    def __init__(self, nums):
        self.pos = 0
        self.nums = nums

    def next(self):
        res = self.nums[self.pos]
        self.pos += 1
        return res

    def hasNext(self):
        return self.pos < len(self.nums)


iterator = Iterator([4, 5, 8, 9, 12])
while iterator.hasNext():
    print(iterator.next())
