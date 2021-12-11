# T=logn
def main(target):
    low, high = 0, target
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid <= target < (mid + 1) * (mid + 1):
            return mid
        elif target > mid * mid:
            low = mid + 1
        else:
            high = mid - 1


for target in [
    0, 1, 4, 8, 9, 10, 2 ** 31 - 1
]:
    print(main(target), end=' ')
