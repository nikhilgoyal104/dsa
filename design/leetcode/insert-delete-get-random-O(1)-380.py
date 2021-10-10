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
        index = self.data.pop(val)
        if index == len(self.helper) - 1:
            self.helper.pop()
            return True
        self.helper[index] = self.helper.pop()
        self.data[self.helper[index]] = index
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
