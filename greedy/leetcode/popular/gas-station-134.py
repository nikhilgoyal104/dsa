inputs = [
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
    ([2, 3, 4], [3, 4, 3])
]


# T=n²,S=1
def main(gas, cost):
    n = len(gas)
    for i in range(n):
        tank = 0
        for j in range(i, i + n):
            tank += (gas[j % n] - cost[j % n])
            if tank < 0:
                break
        if tank >= 0:
            return i
    return -1


for gas, cost in inputs:
    print(main(gas, cost), end=' ')

print()


# T=n,S=1
def main(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    tank = res = 0
    for i in range(len(gas)):
        tank += (gas[i] - cost[i])
        if tank < 0:
            res = i + 1
            tank = 0
    return res


for gas, cost in inputs:
    print(main(gas, cost), end=' ')
