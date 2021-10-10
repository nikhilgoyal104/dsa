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
        if val == self.helper[-1]:
            del self.data[val]
            self.helper.pop()
            return True
        index = self.data.pop(val)
        self.swap(index)
        self.data[self.helper[index]] = index
        self.helper.pop()
        return True

    def getRandom(self):
        return random.choice(self.helper)

    def swap(self, index):
        self.helper[index], self.helper[-1] = self.helper[-1], self.helper[index]


rs = RandomizedSet()
print(rs.insert(1))
print(rs.remove(2))
print(rs.insert(2))
print(rs.getRandom())
print(rs.remove(1))
print(rs.insert(2))
print(rs.getRandom())
