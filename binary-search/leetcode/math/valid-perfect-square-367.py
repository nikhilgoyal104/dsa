def main(n):
    if n == 1:
        return True
    low, high = 1, n // 2
    while low <= high:
        mid = low + (high - low) // 2
        val = mid * mid
        if val == n:
            return True
        elif val > n:
            high = mid - 1
        else:
            low = mid + 1
    return False


for n in [1, 14, 16]:
    print(main(n))
