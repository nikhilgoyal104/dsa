from math import inf

heap = []


def build(nums):
    for val in nums:
        heap.append(val)
    for i in range((len(heap) // 2) - 1, -1, -1):
        downheapify(i)


def downheapify(i):
    n, mini = len(heap), i
    lci = 2 * i + 1
    if lci < n and heap[lci] < heap[mini]:
        mini = lci
    rci = 2 * i + 2
    if rci < n and heap[rci] < heap[mini]:
        mini = rci
    if mini != i:
        heap[i], heap[mini] = heap[mini], heap[i]
        downheapify(mini)


build([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17])
print(heap[0])
