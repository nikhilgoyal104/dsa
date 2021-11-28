class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, i):
        return self.arr[i]


# T=logT,S=1
def main(reader, target):
    low, high = 0, 1
    while reader.get(high) < target:
        low, high = high, 2 * high
    while low <= high:
        mid = low + (high - low) // 2
        val = reader.get(mid)
        if target == val:
            return mid
        elif target > val:
            low = mid + 1
        else:
            high = mid - 1
    return -1


for nums, target in [
    ([-1, 0, 3, 5, 9, 12], 9),
    ([-1, 0, 3, 5, 9, 12], 2),
]:
    print(main(ArrayReader(nums), target))
