def prefixSuffix1(s):
    for i in range(len(s)):
        prefix, suffix = s[:i], s[i:]
        print(prefix, suffix)
    print()


def prefixSuffix2(s):
    for i in range(len(s)):
        prefix, suffix = s[:i + 1], s[i + 1:]
        print(prefix, suffix)
    print()


for s in [
    'abcd',
    'ni',
    'aa',
    'n',
]:
    prefixSuffix1(s)
    prefixSuffix2(s)

s = 'abcd'
for i in range(len(s) + 1):
    print(s[:i], s[i:])
