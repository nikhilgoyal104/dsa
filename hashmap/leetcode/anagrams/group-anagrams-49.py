from collections import defaultdict


# T=NKlogK,S=NK
def x(words):
    group = defaultdict(list)
    for word in words:
        group[''.join(sorted(word))].append(word)
    return group.values()


# T=NK,S=NK
def y(words):
    group = defaultdict(list)
    for word in words:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        group[tuple(count)].append(word)
    return group.values()


for words in [
    ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
    ['pepcoding', 'codingpep', 'pepper', 'rapper', 'repepp'],
    ['a'],
    ['']
]:
    print(x(words), end=' ')
    print(y(words))
