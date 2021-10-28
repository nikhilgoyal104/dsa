def outside(m, n, ri, ci):
    return ri in [-1, m] or ci in [-1, n]


def roll(grid, ri, ci, i, j):
    m, n = len(grid), len(grid[0])
    nri, nci = ri, ci
    while not outside(m, n, nri + i, nci + j) and grid[nri + i][nci + j] != 1:
        nri, nci = nri + i, nci + j
    return nri, nci


def main(grid, sri, sci, dri, dci):
    vis = set()
    offsets = (-1, 0), (0, 1), (1, 0), (0, -1)

    def dfs(ri, ci):
        if (ri, ci) in vis:
            return False
        if (ri, ci) == (dri, dci):
            return True
        vis.add((ri, ci))
        for i, j in offsets:
            nri, nci = roll(grid, ri, ci, i, j)
            if dfs(nri, nci):
                return True
        return False

    print(dfs(sri, sci))


for grid, sri, sci, dri, dci in [
    ([[0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0],
      [1, 1, 0, 1, 1],
      [0, 0, 0, 0, 0]],
     0, 4, 4, 4),
    ([[0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0],
      [1, 1, 0, 1, 1],
      [0, 0, 0, 0, 0]],
     0, 4, 3, 2),
    ([[0, 0, 0, 0, 0],
      [1, 1, 0, 0, 1],
      [0, 0, 0, 0, 0],
      [0, 1, 0, 0, 1],
      [0, 1, 0, 0, 0]],
     4, 3, 0, 1)
]:
    main(grid, sri, sci, dri, dci)
