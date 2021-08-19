from math import inf


def x(intervals):
    intervals.sort(key=lambda x: x[1])
    res, pe = 0, -inf
    for cs, ce in intervals:
        if cs > pe:
            pe, res = ce, res + 1
    return res


for intervals in [
    [[10, 16], [2, 8], [1, 6], [7, 12]],
    [[1, 2], [3, 4], [5, 6], [7, 8]],
    [[1, 2], [2, 3], [3, 4], [4, 5]]
]:
    print(x(intervals), end='')
    print()
