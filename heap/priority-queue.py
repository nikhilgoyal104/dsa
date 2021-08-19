from math import inf

heap = []


def add(data):
    heap.append(data)
    upheapify(len(heap) - 1)


def upheapify(i):
    if i == 0:
        return
    pi = (i - 1) // 2
    if heap[pi] > heap[i]:
        heap[pi], heap[i] = heap[i], heap[pi]
        upheapify(pi)


def remove():
    if not heap:
        return
    heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
    data = heap.pop()
    downheapify(0)
    return data


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
