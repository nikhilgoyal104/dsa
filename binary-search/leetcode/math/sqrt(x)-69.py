def x(tar):
    low, high = 0, tar
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid <= tar < (mid + 1) * (mid + 1):
            return mid
        elif tar > mid * mid:
            low = mid + 1
        else:
            high = mid - 1


for tar in [
    0, 1, 4, 8, 9, 10, 2 ** 31 - 1
]:
    print(x(tar), end=' ')
