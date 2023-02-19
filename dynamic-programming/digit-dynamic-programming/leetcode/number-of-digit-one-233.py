# T=logn,S=logn
def x(n):
    n, cache = str(n), {}
    size = len(n)

    def dfs(i, restrict, oneCount):
        if i == size:
            return oneCount
        key = i, restrict, oneCount
        if key in cache:
            return cache[key]
        cache[key], limit = 0, int(n[i]) if restrict else 9
        for digit in range(limit + 1):
            cache[key] += dfs(i + 1, False if digit < limit else restrict, oneCount + (digit is 1))
        return cache[key]

    return dfs(0, True, 0)


for n in [
    13, 0
]:
    print(x(n))
