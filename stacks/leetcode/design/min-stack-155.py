from math import inf

tests = [
    [5, 7, 2, 3, 1, 1, 6],
    [5, 5, 2, 2, 1, 1, 1],
    [-3, 0, -2],
    [0, 1, 0],
    [12, 30, 7, 6, 45, 6, 6, 14, 6]
]


# T=1,S=n
class MinStack:

    def __init__(self):
        self.main = []
        self.helper = []

    def push(self, val):
        self.main.append(val)
        if not self.helper or val <= self.helper[-1]:
            self.helper.append(val)

    def pop(self):
        if self.main.pop() == self.helper[-1]:
            self.helper.pop()

    def top(self):
        return self.main[-1]

    def min(self):
        return self.helper[-1]


for test in tests:
    stack = MinStack()
    for val in test:
        stack.push(val)
    print(stack.main, stack.helper)

print()


# T=1,S=n
class MinStack:

    def __init__(self):
        self.main = []
        self.helper = []

    def push(self, val):
        self.main.append(val)
        if not self.helper or val < self.helper[-1][0]:
            self.helper.append([val, 1])
        elif val == self.helper[-1][0]:
            self.helper[-1][1] += 1

    def pop(self):
        if self.main.pop() == self.helper[-1]:
            self.helper[-1][1] -= 1
            if not self.helper[-1][1]:
                self.helper.pop()

    def top(self):
        return self.main[-1]

    def min(self):
        return self.helper[-1][0]


for test in tests:
    stack = MinStack()
    for val in test:
        stack.push(val)
    print(stack.main, stack.helper)

print()


class Node:
    def __init__(self, val=0, min=inf, next=None):
        self.val = val
        self.min = min
        self.next = next


# T=1,S=n
class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val):
        if not self.head:
            self.head = Node(val, val)
        else:
            self.head = Node(val, min(self.head.min, val), self.head)

    def pop(self):
        self.head = self.head.next

    def top(self):
        return self.head.val

    def min(self):
        return self.head.min


for test in tests:
    stack = MinStack()
    for val in test:
        stack.push(val)
