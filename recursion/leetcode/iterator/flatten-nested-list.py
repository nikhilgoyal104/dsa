def x(nested):
    res = []

    def dfs(nested):
        for val in nested:
            if type(val) is list:
                dfs(val)
                continue
            res.append(val)

    dfs(nested)
    return res


def y(nested):
    def dfs(nested):
        if not nested:
            return []
        if type(nested[0]) is list:
            return dfs(nested[0]) + dfs(nested[1:])
        return [nested[0]] + dfs(nested[1:])

    return dfs(nested)


def z(nested):
    def dfs(nested):
        res = []
        for val in nested:
            if type(val) is list:
                res += dfs(val)
                continue
            res.append(val)
        return res

    return dfs(nested)


for nested in [
    [],
    [1, 2, 3, 4, 5],
    [[1, 2], [3], [4]],
    [[1, 1], 2, [1, 1]],
    [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
]:
    print(x(nested))
    print(y(nested))
    print(z(nested))
    print()
