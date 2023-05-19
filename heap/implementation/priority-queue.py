heap = []


def add(data):
    heap.append(data)
    _upheapify(len(heap) - 1)


def _upheapify(index):
    if index == 0:
        return
    parentIndex = (index - 1) // 2
    if heap[parentIndex] > heap[index]:
        heap[parentIndex], heap[index] = heap[index], heap[parentIndex]
        _upheapify(parentIndex)


def remove():
    if not heap:
        return
    heap[0], heap[-1] = heap[-1], heap[0]
    data = heap.pop()
    _downheapify(0)
    return data


def _downheapify(index):
    n = len(heap)
    minIndex = index
    leftChildIndex = 2 * index + 1
    if leftChildIndex < n and heap[leftChildIndex] < heap[minIndex]:
        minIndex = leftChildIndex
    rightChildIndex = 2 * index + 2
    if rightChildIndex < n and heap[rightChildIndex] < heap[minIndex]:
        minIndex = rightChildIndex
    if minIndex != index:
        heap[index], heap[minIndex] = heap[minIndex], heap[index]
        _downheapify(minIndex)


def peek():
    if not heap:
        return
    return heap[0]


for data in [10, 20, 30, 40]:
    add(data)

print(peek())
add(50)
for i in range(4):
    print(peek())
    print(remove())

print(peek())
