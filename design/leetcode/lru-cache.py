from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


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
