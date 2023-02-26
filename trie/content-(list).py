class TrieNode:
    def __init__(self):
        self.word = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.word = True


trie = Trie()
for key in ['the', 'a', 'there', 'camera', 'their', 'nikhil', 'b', 'cat']:
    trie.insert(key)


def content(root):
    res = []
    path = []

    def dfs(root):
        if root.word:
            res.append(''.join(path))
        for i in range(26):
            if root.children[i]:
                path.append(chr(i + 97))
                dfs(root.children[i])
                path.pop()

    dfs(root)
    return res


print(content(trie.root))


def content(root):
    res = []

    def dfs(root, path):
        if root.word:
            res.append(''.join(path))
        for i in range(26):
            if root.children[i]:
                dfs(root.children[i], path + chr(i + 97))

    dfs(root, '')
    return res


print(content(trie.root))
