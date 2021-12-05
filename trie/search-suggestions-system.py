inputs = [
    (['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse'),
    (['havana'], 'havana'),
    (['bags', 'baggage', 'banner', 'box', 'cloths'], 'bags'),
    (['havana'], 'tatiana')
]


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

    def getLastNodeInPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def content(self, root, start):
        res = []

        def dfs(root, path):
            if len(res) == 3:
                return
            if root.word:
                res.append(path)
            for child in root.children:
                dfs(root.children[child], path + child)

        dfs(root, start)
        return res

    def getWordsStartingWithPrefix(self, prefix):
        lastNodeInPrefix = self.getLastNodeInPrefix(prefix)
        if not lastNodeInPrefix:
            return []
        return self.content(lastNodeInPrefix, prefix)


def main(products, searchWord):
    res, trie = [], Trie()
    for product in products:
        trie.insert(product)
    for i in range(len(searchWord)):
        res.append(trie.getWordsStartingWithPrefix(searchWord[:i + 1]))
    return res


for products, word in inputs:
    print(main(products, word))
