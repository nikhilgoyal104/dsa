from collections import Counter
from math import inf


# T=n²,S=n
def main(points):
    res, n = 0, len(points)
    for i in range(n):
        x1, y1 = points[i][0], points[i][1]
        slopeFreq = Counter()
        for j in range(i + 1, n):
            x2, y2 = points[j][0], points[j][1]
            num, den = y2 - y1, x2 - x1
            slope = num / den if den else inf
            slopeFreq[slope] += 1
        res = max(res, 1 + max(slopeFreq.values(), default=0))
    return res


for points in [
    [[1, 1], [2, 2], [3, 3]],
    [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
]:
    print(main(points))
