# T=n
def x(n):
    for version in range(1, n + 1):
        if isBadVersion(version):
            return version


# T=logn
def y(n):
    low, high, res = 1, n, 1
    while low <= high:
        mid = low + (high - low) // 2
        if isBadVersion(mid):
            res, high = mid, mid - 1
        else:
            low = mid + 1
    return res
