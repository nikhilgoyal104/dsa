def isPalindrome(s):
    return s == s[::-1]


def x(s):
    def dfs(s):
        if not s:
            return 1
        count = 0
        for i in range(len(s)):
            prefix, suffix = s[:i + 1], s[i + 1:]
            if isPalindrome(prefix):
                count += dfs(suffix)
        return count

    return dfs(s)


for s in [
    'abaaba',
    'nitin',
    'geeks',
    'aab',
    'aaa',
    'a'
]:
    print(x(s))
