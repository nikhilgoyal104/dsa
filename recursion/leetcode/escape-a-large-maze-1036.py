from collections import deque


def main(blocked, source, target):
    if not blocked:
        return True
    blocked = set(map(tuple, blocked))

    def bfs(source, target):
        sri, sci = source
        dri, dci = target
        queue, vis = deque([(sri, sci)]), {(sri, sci)}
        while queue:
            ri, ci = queue.popleft()
            if (ri, ci) == (dri, dci) or abs(ri - sri) == 200 or abs(ci - sci) == 200:
                return True
            for i, j in (1, 0), (0, 1), (-1, 0), (0, -1):
                x, y = ri + i, ci + j
                if x in [-1, 10 ** 6] or y in [-1, 10 ** 6] or (x, y) in vis or (x, y) in blocked:
                    continue
                vis.add((x, y))
                queue.append((x, y))
        return False

    return bfs(source, target) and bfs(target, source)


for blocked, source, target in [
    ([[0, 1], [1, 0]], [0, 0], [0, 2]),
    ([], [0, 0], [999999, 999999]),
    ([[691938, 300406], [710196, 624190], [858790, 609485], [268029, 225806], [200010, 188664], [132599, 612099],
      [329444, 633495], [196657, 757958], [628509, 883388]], [655988, 180910], [267728, 840949])
]:
    print(main(blocked, source, target))
