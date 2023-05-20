inputs = [
    (['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse'),
    (['havana'], 'havana'),
    (['bags', 'baggage', 'banner', 'box', 'cloths'], 'bags'),
    (['havana'], 'tatiana')
]


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
            index = ord(char) - 97
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.word = True

    def _getLastNodeInPrefix(self, word):
        node = self.root
        for char in word:
            index = ord(char) - 97
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

    def content(self, root, prefix):
        res = []

        def dfs(root, prefix):
            if len(res) == 3:
                return
            if root.word:
                res.append(prefix)
            for i in range(26):
                if root.children[i]:
                    dfs(root.children[i], prefix + chr(i + 97))

        dfs(root, prefix)
        return res

    def getWordsStartingWithPrefix(self, prefix):
        lastNodeInPrefix = self._getLastNodeInPrefix(prefix)
        if not lastNodeInPrefix:
            return []
        return self.content(lastNodeInPrefix, prefix)


def main(products, searchWord):
    res = []
    trie = Trie()
    for product in products:
        trie.insert(product)
    for i in range(len(searchWord)):
        res.append(trie.getWordsStartingWithPrefix(searchWord[:i + 1]))
    return res


for products, word in inputs:
    print(main(products, word))

print()


def main(products, searchWord):
    res = []
    products = sorted(products)
    for i in range(len(searchWord)):
        matching = []
        for product in products:
            if product.startswith(searchWord[:i + 1]) and len(matching) < 3:
                matching.append(product)
        res.append(matching)
    return res


for products, word in inputs:
    print(main(products, word))
