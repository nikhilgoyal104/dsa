class CustomStack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, val):
        if len(self.stack) < self.capacity:
            self.stack.append(val)

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k, val):
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


stack = CustomStack(3)
stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(2)
stack.push(3)
stack.push(4)
stack.increment(5, 100)
stack.increment(2, 100)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print()


class CustomStack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, val):
        if len(self.stack) < self.capacity:
            self.stack.append([val, 0])

    def pop(self):
        if not self.stack:
            return -1
        val, inc = self.stack.pop()
        if self.stack:
            self.stack[-1][1] += inc
        return val + inc

    def increment(self, k, val):
        if self.stack:
            self.stack[min(k, len(self.stack)) - 1][1] += val


stack = CustomStack(3)
stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(2)
stack.push(3)
stack.push(4)
stack.increment(5, 100)
stack.increment(2, 100)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
