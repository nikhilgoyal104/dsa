def main(n):
    def dfs(start, sum, path):
        if sum == n:
            return 1
        if sum < 0:
            return 0
        res = 0
        for i in range(start, n + 1):
            if not path or path[-1] + 1 == i:
                res += dfs(i + 1, sum + i, path + [i])
        return res

    return dfs(1, 0, [])


for n in [
    4, 5, 7, 8, 9, 15
]:
    print(main(n))
