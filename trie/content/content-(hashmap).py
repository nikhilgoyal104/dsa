class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
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
        for char, node in root.children.items():
            path.append(char)
            dfs(node)
            path.pop()

    dfs(root)
    return res


print(content(trie.root))


def content(root):
    res = []

    def dfs(root, path):
        if root.word:
            res.append(path)
        for char, node in root.children.items():
            dfs(node, path + char)

    dfs(root, '')
    return res


print(content(trie.root))
