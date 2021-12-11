from heapq import *

inputs = [
    [[1, 5, 7, 8], [12, 45, 67, 98], [1, 2, 5, 7]],
    [[2, 4], [3, 5, 7], [1, 10, 11, 12]],
    [[3, 5, 7], [0, 6], [0, 6, 28]],
    [[3, 5, 7], [0, 6], [], [0, 6, 28]],
]


# T=Nlog(N),S=N
def main(arrays):
    res = []
    for array in arrays:
        for val in array:
            res.append(val)
    return sorted(res)


for arrays in inputs:
    print(main(arrays))

print()


def merge(nums, b):
    m, n = len(nums), len(b)
    res, i, j = [], 0, 0
    while i < m and j < n:
        if nums[i] < b[j]:
            res.append(nums[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < m:
        res.append(nums[i])
        i += 1
    while j < n:
        res.append(b[j])
        j += 1
    return res


# T=Nk,S=N
def main(arrays):
    merged = arrays[0]
    for i in range(1, len(arrays)):
        merged = merge(merged, arrays[i])
    return merged


for arrays in inputs:
    print(main(arrays))

print()


# T=k+Nlogk,S=k+N
def main(arrays):
    res, heap = [], []
    for arr in arrays:
        if arr:
            heap.append((arr[0], 0, arr))
    heapify(heap)
    while heap:
        val, i, arr = heappop(heap)
        res.append(val)
        if i + 1 < len(arr):
            heappush(heap, (arr[i + 1], i + 1, arr))
    return res


for arrays in inputs:
    print(main(arrays))
