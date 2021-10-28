# T=n²,S=n
# dp[i] length of LIS ending with nums[i]
def main(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    return n - max(dp)


for nums in [
    [4, 2, 3, 6, 10, 1, 12],
    [-4, 10, 3, 7, 15],
    [3, 2, 1, 0]
]:
    print(main(nums))
