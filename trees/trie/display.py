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

    def content(self):
        path, words = [], []

        def dfs(root):
            path.append(root.val)
            if root.word:
                words.append(''.join(path))
            for child in root.children:
                if child:
                    dfs(child)
            path.pop()

        dfs(self.root)
        return words


keys = ['the', 'a', 'there', 'their']
trie = Trie()
for key in keys:
    trie.insert(key)

print(trie.content())
