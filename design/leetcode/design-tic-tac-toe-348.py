# T=4n,S=4n
class TicTacToe:

    def __init__(self, n):
        self.n = n
        self.p1RowCount = [0] * n
        self.p1ColCount = [0] * n
        self.p2RowCount = [0] * n
        self.p2ColCount = [0] * n
        self.p1DiagCount = self.p1AntiDiagCount = 0
        self.p2DiagCount = self.p2AntiDiagCount = 0

    def p1Wins(self):
        return self.n in self.p1RowCount or self.n in self.p1ColCount or self.n in [self.p1DiagCount,
                                                                                    self.p1AntiDiagCount]

    def p2Wins(self):
        return self.n in self.p2RowCount or self.n in self.p2ColCount or self.n in [self.p2DiagCount,
                                                                                    self.p2AntiDiagCount]

    def move(self, row, col, player):
        if player == 1:
            self.p1RowCount[row] += 1
            self.p1ColCount[col] += 1
            if row == col:
                self.p1DiagCount += 1
            if row + col == self.n - 1:
                self.p1AntiDiagCount += 1
        else:
            self.p2RowCount[row] += 1
            self.p2ColCount[col] += 1
            if row == col:
                self.p2DiagCount += 1
            if row + col == self.n - 1:
                self.p2AntiDiagCount += 1
        if self.p1Wins():
            return 1
        if self.p2Wins():
            return 2
        return 0


tic = TicTacToe(n=3)
for row, col, player in [
    [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]
]:
    print(tic.move(row, col, player))


# T=1,S=2n
class TicTacToe:

    def __init__(self, n):
        self.n = n
        self.rowCount = [0] * n
        self.colCount = [0] * n
        self.diag = self.antiDiag = 0

    def move(self, row, col, player):
        val = 1 if player == 1 else -1
        self.rowCount[row] += val
        self.colCount[col] += val
        if row == col:
            self.diag += val
        if row + col == self.n - 1:
            self.antiDiag += val
        if self.n in [abs(self.rowCount[row]), abs(self.colCount[col]), abs(self.diag), abs(self.antiDiag)]:
            return player
        return 0


tic = TicTacToe(n=3)
for row, col, player in [
    [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]
]:
    print(tic.move(row, col, player))
