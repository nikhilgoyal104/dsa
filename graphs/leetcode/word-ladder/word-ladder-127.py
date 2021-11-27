from collections import deque


# T=NL²26,S=NL²
def main(beginWord, endWord, wordList):
    wordList = set(wordList)
    queue, vis = deque([(beginWord, 1)]), set()
    while queue:
        word, dist = queue.popleft()
        if word == endWord:
            return dist
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                nbr = word[:i] + char + word[i + 1:]
                if nbr in wordList and nbr not in vis:
                    vis.add(nbr)
                    queue.append((nbr, dist + 1))
    return 0


for beginWord, endWord, wordList in [
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']),
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']),
]:
    print(main(beginWord, endWord, wordList))
