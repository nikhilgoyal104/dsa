inputs = [
    (['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse')
]


def main(products, word):
    res = []
    for i in range(len(word)):
        subList = []
        for product in products:
            if product.startswith(word[:i + 1]):
                subList.append(product)
        subList.sort()
        res.append(subList[:3])
    return res


for products, word in inputs:
    print(main(products, word))


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = [None] * 26


# T=m to build trie where m=total number of characters in products
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


def main(products, word):
    print(products)


for products, word in inputs:
    print(main(products, word))
