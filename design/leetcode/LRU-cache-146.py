class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def delete(self, node):
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

    def addAtFront(self, key, value):
        if not self.head:
            self.head = self.tail = Node(key, value)
            return self.head
        node = Node(key, value, next=self.head)
        self.head.prev = node
        self.head = node
        return self.head


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.dll = DoublyLinkedList()
        self.cache = {}

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache[key].val
        self._delete(key=key, address=self.cache[key])
        self._add(key, value)
        return value

    def put(self, key, value):
        if key in self.cache:
            self._delete(key=key, address=self.cache[key])
        elif self._isFull():
            self._delete(key=self.dll.tail.key, address=self.dll.tail)
        self._add(key, value)

    def _delete(self, key, address):
        del self.cache[key]
        self.dll.delete(address)

    def _add(self, key, value):
        self.cache[key] = self.dll.addAtFront(key, value)

    def _isFull(self):
        return len(self.cache) == self.capacity


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))
lru.put(3, 3)
print(lru.get(2))
lru.put(4, 4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))
print()

lru = LRUCache(3)
lru.put(1, 10)
lru.put(2, 20)
lru.put(3, 30)
print(lru.get(1))
lru.put(1, 15)
print(lru.get(1))
print(lru.get(2))
lru.put(4, 40)
print(lru.get(3))
print(lru.get(4))
