from math import inf

heap = []


def build(nums):
    for val in nums:
        heap.append(val)
    for i in range((len(heap) // 2) - 1, -1, -1):
        downheapify(i)


def downheapify(index):
    n, minIndex = len(heap), index
    leftChildIndex = 2 * index + 1
    if leftChildIndex < n and heap[leftChildIndex] < heap[minIndex]:
        minIndex = leftChildIndex
    rightChildIndex = 2 * index + 2
    if rightChildIndex < n and heap[rightChildIndex] < heap[minIndex]:
        minIndex = rightChildIndex
    if minIndex != index:
        heap[index], heap[minIndex] = heap[minIndex], heap[index]
        downheapify(minIndex)


build([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17])
print(heap[0])
