# T=mn,S=1
def v(grid, target):
    for row in grid:
        if target in row:
            return True
    return False


# T=mlogn,S=1
def w(grid, target):
    def search(nums):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == mid:
                return True
            elif target > mid:
                low = mid + 1
            else:
                high = mid - 1
        return False

    for row in grid:
        if search(row):
            return True
    return False


# T=m+n,S=1
def x(grid, target):
    m, n = len(grid), len(grid[0])
    ri, ci = 0, n - 1
    while ri < m and ci > -1:
        if target == grid[ri][ci]:
            return True
        elif target > grid[ri][ci]:
            ri += 1
        else:
            ci -= 1
    return False


# T=log(mn),S=1
def y(grid, target):
    m, n = len(grid), len(grid[0])
    low, high = 0, m * n - 1
    while low <= high:
        mid = low + (high - low) // 2
        val = grid[mid // n][mid % n]
        if target == val:
            return True
        elif target > val:
            low = mid + 1
        else:
            high = mid - 1
    return False


def potential(grid, target):
    low, high = 0, len(grid) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if grid[mid][0] <= target <= grid[mid][-1]:
            return mid
        if target < grid[mid][0]:
            high = mid - 1
        elif target > grid[mid][-1]:
            low = mid + 1
    return -1


def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return True
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


# T=log(mn),S=1
def z(grid, target):
    ri = potential(grid, target)
    return search(grid[ri], target) if ri != -1 else False


for grid, target in [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
]:
    print(v(grid, target), end=' ')
    print(w(grid, target), end=' ')
    print(x(grid, target), end=' ')
    print(y(grid, target), end=' ')
    print(z(grid, target))
