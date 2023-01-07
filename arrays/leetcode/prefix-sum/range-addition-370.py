inputs = [
    (5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]),
    (10, [[2, 4, 6], [5, 6, 8], [1, 9, -4]])
]


# T=kn,S=1
def main(length, updates):
    res = [0] * length
    for start, end, val in updates:
        for i in range(start, end + 1):
            res[i] += val
    return res


for length, updates in inputs:
    print(main(length, updates))

print()


# T=k+n,S=1
def main(length, updates):
    res = [0] * length
    for start, end, val in updates:
        res[start] += val
        if end < length - 1:
            res[end + 1] -= val
    sum = 0
    for i in range(length):
        sum += res[i]
        res[i] = sum
    return res


for length, updates in inputs:
    print(main(length, updates))
