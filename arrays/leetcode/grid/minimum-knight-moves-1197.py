from collections import deque


def main(dri, dci):
    queue, vis = deque([(0, 0, 0)]), {(0, 0)}
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)
    while queue:
        ri, ci, dist = queue.popleft()
        if (ri, ci) == (dri, dci):
            return dist
        for i, j in offsets:
            x, y = ri + i, ci + j
            if (x, y) not in vis:
                vis.add((x, y))
                queue.append((x, y, dist + 1))
    return -1


for dri, dci in [
    (2, 1), (5, 5)
]:
    print(main(dri, dci))
