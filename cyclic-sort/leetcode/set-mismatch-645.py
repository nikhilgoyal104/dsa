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
            return [nums[presentIndex], presentIndex + 1]


for nums in [
    [4, 3, 4, 5, 1],
    [4, 3, 5, 4, 1],
    [1, 2, 2, 4],
    [1, 1]
]:
    print(main(nums))
