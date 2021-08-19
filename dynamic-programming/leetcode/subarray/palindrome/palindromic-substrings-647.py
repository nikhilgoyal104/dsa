def isPalindrome(s):
    low, high = 0, len(s) - 1
    while low < high:
        if s[low] != s[high]:
            return False
        low, high = low + 1, high - 1
    return True


# T=n³,S=1
def x(s):
    res, n = 0, len(s)
    for i in range(n):
        for j in range(i, n):
            res += isPalindrome(s[i:j + 1])
    return res


# T=n²,S=n²
# dp[i][j] = is s[i:j+1] a palindrome
def y(s):
    n = len(s)
    res, dp = 0, [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
            res += dp[i][j]
    return res


# T=n²,S=1
def z(s):
    n = len(s)

    def expand(low, high):
        count = 0
        while -1 < low and high < n and s[low] == s[high]:
            low, high, count = low - 1, high + 1, count + 1
        return count

    return sum(expand(i, i) + expand(i, i + 1) for i in range(n))


for s in [
    'a',
    'bb',
    'abc',
    'aaa',
    'abba',
    'madam',
    'abccbc'
]:
    print(str(s) + '->', end='')
    print(x(s), end=' ')
    print(y(s), end=' ')
    print(z(s))
