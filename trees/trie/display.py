class TrieNode:
    def __init__(self, val):
        self.val = val
        self.word = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode(char)
            node = node.children[index]
        node.word = True


keys = ['the', 'a', 'there', 'their', 'nikhil', 'b']
trie = Trie()
for key in keys:
    trie.insert(key)


def content(root):
    path, res = [], []

    def dfs(root):
        path.append(root.val)
        if root.word:
            res.append(''.join(path))
        for child in root.children:
            if child:
                dfs(child)
        path.pop()

    dfs(root)
    return res


print(content(trie.root))


def content(root):
    res = []

    def dfs(root, path):
        if root.word:
            res.append(path)
        for child in root.children:
            if child:
                dfs(child, path + child.val)

    dfs(root, '')
    return res


print(content(trie.root))
