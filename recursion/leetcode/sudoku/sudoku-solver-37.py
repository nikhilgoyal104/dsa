# T=nn!,S=n²
def main(grid):
    values, vis, n = '123456789', set(), 9

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val != '.':
                vis.update({(i, val), (val, j), (i // 3, j // 3, val)})

    def dfs(ri, ci):
        if ri == n:
            return True
        nri, nci = (ri + 1, 0) if ci == n - 1 else (ri, ci + 1)
        if grid[ri][ci] != '.':
            return dfs(nri, nci)
        for val in values:
            submatrix = (ri // 3, ci // 3, val)
            if (ri, val) in vis or (val, ci) in vis or submatrix in vis:
                continue
            vis.update({(ri, val), (val, ci), submatrix})
            grid[ri][ci] = val
            if dfs(nri, nci):
                return True
            grid[ri][ci] = '.'
            vis.difference_update({(ri, val), (val, ci), submatrix})
        return False

    dfs(0, 0)


for grid in [
    [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
]:
    main(grid)
    print(grid)
