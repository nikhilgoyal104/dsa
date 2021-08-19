from collections import deque
from math import inf


def outside(m, n, ri, ci):
    return ri > m - 1 or ci > n - 1 or ri < 0 or ci < 0


# T=n²,S=n²
def bfs(m, n, sri, sci, dri, dci):
    offsets = (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)
    queue, vis = deque([(sri, sci, 0)]), {(sri, sci)}
    while queue:
        ri, ci, dist = queue.popleft()
        if (ri, ci) == (dri, dci):
            return dist
        for i, j in offsets:
            x, y = ri + i, ci + j
            if outside(m, n, x, y) or (x, y) in vis:
                continue
            vis.add((x, y))
            queue.append((x, y, dist + 1))


def main(m, n, sri, sci, dri, dci):
    print(bfs(m, n, sri, sci, dri, dci))


for m, n, sri, sci, dri, dci in [
    (3, 3, 0, 0, 2, 2),
    (8, 8, 7, 0, 0, 7)
]:
    main(m, n, sri, sci, dri, dci)
