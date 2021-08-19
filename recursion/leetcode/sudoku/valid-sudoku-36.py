def isValidSubBox(grid, startRow, startCol):
    vis = set()
    for i in range(startRow, startRow + 3):
        for j in range(startCol, startCol + 3):
            if grid[i][j] in vis:
                return False
            vis.add(grid[i][j] if grid[i][j] != '.' else None)
    return True


# T=n²,S=n²
def x(grid):
    n = 9
    for i in range(n):
        vis = set()
        for j in range(n):
            if grid[i][j] in vis:
                return False
            vis.add(grid[i][j] if grid[i][j] != '.' else None)

    for j in range(n):
        vis = set()
        for i in range(n):
            if grid[i][j] in vis:
                return False
            vis.add(grid[i][j] if grid[i][j] != '.' else None)

    for startRow in (0, 3, 6):
        for startCol in (0, 3, 6):
            if not isValidSubBox(grid, startRow, startCol):
                return False
    return True


# T=n²,S=n²
def y(grid):
    vis = set()
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == '.':
                continue
            if (i, val) in vis or (val, j) in vis or (i // 3, j // 3, val) in vis:
                return False
            vis.update({(i, val), (val, j), (i // 3, j // 3, val)})
    return True


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
    ],
    [
        ['.', '.', '.', '.', '5', '.', '.', '1', '.'],
        ['.', '4', '.', '3', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '3', '.', '.', '1'],
        ['8', '.', '.', '.', '.', '.', '.', '2', '.'],
        ['.', '.', '2', '.', '7', '.', '.', '.', '.'],
        ['.', '1', '5', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '2', '.', '9', '.', '.', '.', '.', '.'],
        ['.', '.', '4', '.', '.', '.', '.', '.', '.']
    ],
    [
        ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
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
    print(x(grid), end=' ')
    print(y(grid))
