def main(d, low, high):
    def helper(n):
        n, cache = str(n), {}
        size = len(n)

        def dfs(i, restrict, isPreviousDigitZero, digitCount):
            if i == size:
                return digitCount
            key = i, restrict, isPreviousDigitZero, digitCount
            if key in cache:
                return cache[key]
            cache[key], limit = 0, int(n[i]) if restrict else 9
            for digit in range(limit + 1):
                restrictParam = False if digit < limit else restrict
                isPreviousDigitZeroParam = isPreviousDigitZero and not digit
                digitCountParam = digitCount if isPreviousDigitZeroParam else digitCount + (digit is d)
                cache[key] += dfs(i + 1, restrictParam, isPreviousDigitZeroParam, digitCountParam)
            return cache[key]

        return dfs(0, True, True, 0)

    return helper(high) - helper(low - 1)


for d, low, high in [
    (1, 1, 13),
    (3, 100, 250),
    (0, 1, 10)
]:
    print(main(d, low, high))
