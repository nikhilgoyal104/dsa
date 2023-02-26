# T=n²,S=1
def x(gas, cost):
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


# T=n,S=1
def y(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    tank = res = 0
    for i in range(len(gas)):
        tank += (gas[i] - cost[i])
        if tank < 0:
            res = i + 1
            tank = 0
    return res


for gas, cost in [
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
    ([2, 3, 4], [3, 4, 3])
]:
    print(x(gas, cost), end=' ')
    print(y(gas, cost))
