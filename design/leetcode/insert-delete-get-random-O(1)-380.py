import random


class RandomizedSet:

    def __init__(self):
        self.helper = []
        self.data = {}

    def insert(self, val):
        if val in self.data:
            return False
        self.data[val] = len(self.helper)
        self.helper.append(val)
        return True

    def remove(self, val):
        if val not in self.data:
            return False
        last = self.helper[-1]
        index = self.data[val]
        self.helper[index] = last
        self.data[last] = index
        self.helper.pop()
        del self.data[val]
        return True

    def getRandom(self):
        return random.choice(self.helper)


rs = RandomizedSet()
print(rs.insert(1))
print(rs.remove(2))
print(rs.insert(2))
print(rs.getRandom())
print(rs.remove(1))
print(rs.insert(2))
print(rs.getRandom())
