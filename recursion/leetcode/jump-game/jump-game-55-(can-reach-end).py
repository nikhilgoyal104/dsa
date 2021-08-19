# T=n²,S=n
def w(nums):
    target = len(nums) - 1
    dp = {target: True}

    def dfs(i):
        if i in dp:
            return dp[i]
        dp[i] = False
        for val in range(min(nums[i], target - i), 0, -1):
            if dfs(i + val):
                dp[i] = True
                return True
        return False

    return dfs(0)


# T=n²,S=n
def x(nums):
    n = len(nums)
    dp = [False] * n
    dp[0] = True
    for i in range(1, n):
        for j in range(i):
            if dp[j] and j + nums[j] >= i:
                dp[i] = True
                break
    return dp[-1]


# T=n²,S=n
def y(nums):
    n = len(nums)
    dp = [False] * n
    dp[-1] = True
    for i in range(n - 2, -1, -1):
        for j in range(1, nums[i] + 1):
            if i + j < n and dp[i + j]:
                dp[i] = True
                break
    return dp[0]


# T=n,S=1
def z(nums):
    mri = 0
    for i in range(len(nums)):
        if i > mri:
            return False
        mri = max(mri, i + nums[i])
    return True


for nums in [
    [2, 3, 1, 1, 4],
    [3, 2, 1, 0, 4],
    [2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0,
     3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7,
     1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6],

]:
    print(w(nums), end=' ')
    print(x(nums), end=' ')
    print(y(nums), end=' ')
    print(z(nums))
