# T=n,S=1
def main(nums):
    n = len(nums)
    presentIndex = 0
    while presentIndex < n:
        correctIndex = nums[presentIndex] - 1
        if -1 < correctIndex < n and nums[presentIndex] != nums[correctIndex]:
            nums[correctIndex], nums[presentIndex] = nums[presentIndex], nums[correctIndex]
        else:
            presentIndex += 1
    for presentIndex in range(n):
        if presentIndex != nums[presentIndex] - 1:
            return presentIndex + 1
    return None


for nums in [
    [3, 2, 4, 42, 1],
    [3, 2, 4, 5, 78],
    [1, 2, 4, 3],
    [2, 1, 3]
]:
    print(main(nums), nums)
