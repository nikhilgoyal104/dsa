s = 'abcd'
n = len(s)
for i in range(n):
    print(s[:i] + s[i + 1:], end='|')
