from sortedcontainers import SortedDict

tests = [
    [42, 1, 2, 7, 8, 3, 6, 4],
    [42, 7, 8, 9],
    [5, 1],
    [5, 1, 5]
]


# T=n,S=n
class MaxStack:
    def __init__(self):
        self.main = []
        self.helper = []

    def push(self, val):
        self.main.append(val)
        if not self.helper or val >= self.helper[-1]:
            self.helper.append(val)

    def pop(self):
        top = self.main.pop()
        if top == self.helper[-1]:
            self.helper.pop()
        return top

    def top(self):
        return self.main[-1]

    def peekMax(self):
        return self.helper[-1]

    def popMax(self):
        maxVal, buffer = self.helper[-1], []
        while self.top() != maxVal:
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return maxVal


for test in tests:
    stack = MaxStack()
    for val in test:
        stack.push(val)
    print(stack.popMax(), stack.peekMax())

print()


class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def addAtFront(self, val):
        if not self.head:
            self.head = Node(val)
            return self.head
        node = Node(val, next=self.head)
        self.head.prev = node
        self.head = node
        return self.head

    def delete(self, node):
        if node is self.head:
            self.head = node.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev


# T=logn,S=n
class MaxStack:

    def __init__(self):
        self.map = SortedDict()
        self.dll = DoublyLinkedList()

    def push(self, val):
        node = self.dll.addAtFront(val)
        if val not in self.map:
            self.map[val] = []
        self.map[val].append(node)

    def pop(self):
        node = self.dll.head
        self.dll.delete(node)
        addressList = self.map[node.val]
        addressList.pop()
        if not addressList:
            del self.map[node.val]
        return node.val

    def top(self):
        return self.dll.head.val

    def peekMax(self):
        return self.map.peekitem()[0]

    def popMax(self):
        maxVal, addressList = self.map.peekitem()
        self.dll.delete(addressList.pop())
        if not addressList:
            self.map.popitem()
        return maxVal


for test in tests:
    stack = MaxStack()
    for val in test:
        stack.push(val)
    print(stack.popMax(), stack.peekMax())
