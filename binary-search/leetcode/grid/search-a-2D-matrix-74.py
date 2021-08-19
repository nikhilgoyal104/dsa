# T=mn,S=1
def v(grid, tar):
    for row in grid:
        if tar in row:
            return True
    return False


# T=mlogn,S=1
def w(grid, tar):
    def search(nums):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if tar == mid:
                return True
            elif tar > mid:
                low = mid + 1
            else:
                high = mid - 1
        return False

    for row in grid:
        if search(row):
            return True
    return False


# T=m+n,S=1
def x(grid, tar):
    m, n = len(grid), len(grid[0])
    ri, ci = 0, n - 1
    while ri < m and ci > -1:
        if tar == grid[ri][ci]:
            return True
        elif tar > grid[ri][ci]:
            ri += 1
        else:
            ci -= 1
    return False


# T=log(mn),S=1
def y(grid, tar):
    m, n = len(grid), len(grid[0])
    low, high = 0, m * n - 1
    while low <= high:
        mid = low + (high - low) // 2
        val = grid[mid // n][mid % n]
        if tar == val:
            return True
        elif tar > val:
            low = mid + 1
        else:
            high = mid - 1
    return False


def potential(grid, tar):
    low, high = 0, len(grid) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if grid[mid][0] <= tar <= grid[mid][-1]:
            return mid
        if tar < grid[mid][0]:
            high = mid - 1
        elif tar > grid[mid][-1]:
            low = mid + 1
    return -1


def search(grid, tar, ri):
    nums = grid[ri]
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if tar == nums[mid]:
            return True
        elif tar > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


# T=log(mn),S=1
def z(grid, tar):
    ri = potential(grid, tar)
    return search(grid, tar, ri) if ri != -1 else False


for grid, tar in [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
]:
    print(v(grid, tar), end=' ')
    print(w(grid, tar), end=' ')
    print(x(grid, tar), end=' ')
    print(y(grid, tar), end=' ')
    print(z(grid, tar))
