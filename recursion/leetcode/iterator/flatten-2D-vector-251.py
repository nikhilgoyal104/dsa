class Vector2D:

    def __init__(self, vec):
        self.pos = 0
        self.nums = [val for sublist in vec for val in sublist]

    def next(self) -> int:
        res = self.nums[self.pos]
        self.pos += 1
        return res

    def hasNext(self) -> bool:
        return self.pos < len(self.nums)


vector = Vector2D([[1, 2], [3], [4]])
print(vector.next())
print(vector.next())
print(vector.next())
print(vector.hasNext())
print(vector.hasNext())
print(vector.next())
print(vector.hasNext())


class Vector2D:

    def __init__(self, vec):
        self.pos = 0
        self.nums = [val for sublist in vec for val in sublist]

    def next(self) -> int:
        res = self.nums[self.pos]
        self.pos += 1
        return res

    def hasNext(self) -> bool:
        return self.pos < len(self.nums)


vector = Vector2D([[1, 2], [3], [4]])
print(vector.next())
print(vector.next())
print(vector.next())
print(vector.hasNext())
print(vector.hasNext())
print(vector.next())
print(vector.hasNext())
