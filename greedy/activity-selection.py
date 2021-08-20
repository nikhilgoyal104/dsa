from math import inf


def x(intervals):
    intervals.sort(key=lambda x: x[1])
    res, pe = [], -inf
    for i, (cs, ce) in enumerate(intervals):
        if cs >= pe:
            pe = ce
            res.append(i)
    return res


for intervals in [
    [[10, 20], [12, 25], [20, 30]],
    [[1, 2], [3, 4], [0, 6], [5, 7], [8, 9], [5, 9]],
]:
    print(x(intervals), end='')
    print()
