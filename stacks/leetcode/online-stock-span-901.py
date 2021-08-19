tests = [
    [100, 80, 60, 70, 60, 75, 85]
]


# T=n,S=n
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = 0

    def next(self, price):
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        res = self.index - self.stack[-1][0] if self.stack else self.index + 1
        self.stack.append((self.index, price))
        self.index += 1
        return res


for test in tests:
    stock = StockSpanner()
    for price in test:
        print(stock.next(price), end=' ')
    print()
