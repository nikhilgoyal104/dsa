from typing import List


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass


vector = Vector2D([[1, 2], [3], [4]])
print(vector.next())
print(vector.next())
print(vector.next())
print(vector.hasNext())
print(vector.hasNext())
print(vector.next())
print(vector.hasNext())

vec = [[1, 2], [3], [4]]
