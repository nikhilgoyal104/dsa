def x(s):
    vowels, res = 'aeiou', []
    for char in s:
        if char not in vowels:
            res.append(char)
    return ''.join(res)


def y(s):
    return ''.join(char for char in s if char not in 'aeiou')


for s in [
    'leetcodeisacommunityforcoders',
    'aeiou'
]:
    print(x(s), end=' ')
    print(y(s))
