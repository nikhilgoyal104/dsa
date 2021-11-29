inputs = [
    (
        [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], 'ABCCED'),
    (
        [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], 'SEE'),
    (
        [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], 'ABCB')
]


# T=N3ᴸ,S=L
def main(grid, word):
    m, n = len(grid), len(grid[0])
    offsets = (0, 1), (1, 0), (-1, 0), (0, -1)

    def dfs(ri, ci, word, vis):
        if not word:
            return True
        if ri in [-1, m] or ci in [-1, n] or (ri, ci) in vis or word[0] != grid[ri][ci]:
            return False
        vis.add((ri, ci))
        for i, j in offsets:
            if dfs(ri + i, ci + j, word[1:], vis):
                return True
        vis.remove((ri, ci))
        return False

    for i in range(m):
        for j in range(n):
            if word[0] == grid[i][j] and dfs(i, j, word, set()):
                return True
    return False


for grid, word in inputs:
    print(main(grid, word), end=' ')

print()


# T=N3ᴸ,S=L
def main(grid, word):
    m, n = len(grid), len(grid[0])
    offsets = (0, 1), (1, 0), (-1, 0), (0, -1)

    def dfs(ri, ci, word):
        if not word:
            return True
        if ri in [-1, m] or ci in [-1, n] or word[0] != grid[ri][ci]:
            return False
        char = grid[ri][ci]
        grid[ri][ci] = '1'
        res = False
        for i, j in offsets:
            res = dfs(ri + i, ci + j, word[1:])
            if res:
                break
        grid[ri][ci] = char
        return res

    for i in range(m):
        for j in range(n):
            if word[0] == grid[i][j] and dfs(i, j, word):
                return True
    return False


for grid, word in inputs:
    print(main(grid, word), end=' ')
