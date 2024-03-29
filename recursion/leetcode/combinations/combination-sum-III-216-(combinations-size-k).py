# T=kⁿcₖ,S=kⁿcₖ
def main(k, n):
    total = n
    nums = [i for i in range(1, 10)]

    def dfs(start, sum, size):
        if sum == total and size == k:
            return [[]]
        if sum > total:
            return []
        res = []
        for i in range(start, 9):
            for path in dfs(i + 1, sum + nums[i], size + 1):
                res.append([nums[i]] + path)
        return res

    return dfs(0, 0, 0)


for k, n in [
    (3, 7), (3, 9), (4, 1), (3, 2), (9, 45)
]:
    print(main(k, n))
