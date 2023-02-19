# T=n²,S=n
# cache[i] length of LIS ending with nums[i]
def main(nums):
    n = len(nums)
    cache = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                cache[i] = max(cache[i], 1 + cache[j])
    return n - max(cache)


for nums in [
    [4, 2, 3, 6, 10, 1, 12],
    [-4, 10, 3, 7, 15],
    [3, 2, 1, 0]
]:
    print(main(nums))
