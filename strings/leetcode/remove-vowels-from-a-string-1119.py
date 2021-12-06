inputs = [
    'leetcodeisacommunityforcoders',
    'aeiou'
]


def main(s):
    vowels, res = 'aeiou', []
    for char in s:
        if char not in vowels:
            res.append(char)
    return ''.join(res)


for s in inputs:
    print(main(s), end=' ')

print()


def main(s):
    return ''.join(char for char in s if char not in 'aeiou')


for s in inputs:
    print(main(s), end=' ')
