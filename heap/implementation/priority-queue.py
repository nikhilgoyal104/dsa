# T=logn
def heappush(heap, data):
    heap.append(data)
    _upheapify(len(heap) - 1)


def _upheapify(index):
    if index == 0:
        return
    parentIndex = (index - 1) // 2
    if heap[parentIndex] > heap[index]:
        _swap(index, parentIndex)
        _upheapify(parentIndex)


def _swap(i, j):
    heap[i], heap[j] = heap[j], heap[i]


# T=logn
def heappop(heap):
    if not heap:
        return
    _swap(0, -1)
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
        _swap(index, minIndex)
        _downheapify(minIndex)


heap = []
for val in [1, 2, 3, 4]:
    heappush(heap, val)

print(heap[0])
heappush(heap, 5)
print()
for _ in range(4):
    print(heap[0], end=' ')
    print(heappop(heap))
