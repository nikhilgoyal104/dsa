from collections import defaultdict

inputs = [
    ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
    ['pepcoding', 'codingpep', 'pepper', 'rapper', 'repepp'],
    ['a'],
    ['']
]


# T=NKlogK,S=NK
def main(words):
    group = defaultdict(list)
    for word in words:
        group[''.join(sorted(word))].append(word)
    return group.values()


for words in inputs:
    print(main(words))

print()


# T=NK,S=NK
def main(words):
    group = defaultdict(list)
    for word in words:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        group[tuple(count)].append(word)
    return group.values()


for words in inputs:
    print(main(words))
