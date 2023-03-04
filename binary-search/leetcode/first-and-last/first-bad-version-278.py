# T=n
def x(n):
    for version in range(1, n + 1):
        if isBadVersion(version):
            return version


# T=logn
def y(n):
    res = low = 1
    high = n
    while low <= high:
        mid = low + (high - low) // 2
        if isBadVersion(mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
