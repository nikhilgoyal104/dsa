def knows(a, b):
    return True


def isCeleb(i):
    for j in range(n):
        if i == j:
            continue
        if knows(i, j) or not knows(j, i):
            return False
        return True


# T=n²,S=1
def x(n):
    for i in range(n):
        if isCeleb(i):
            return i
    return -1


# T=n,S=1
def y(n):
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    if isCeleb(candidate):
        return candidate
    return -1


for n in [
    4
]:
    print(x(n))
    print(y(n))
