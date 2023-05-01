# T=n,S=1
def main(nums):
    n = len(nums)
    presentIndex = 0
    while presentIndex < n:
        correctIndex = nums[presentIndex] - 1
        if nums[presentIndex] != nums[correctIndex]:
            nums[correctIndex], nums[presentIndex] = nums[presentIndex], nums[correctIndex]
        else:
            presentIndex += 1


for nums in [
    [],
    [1],
    [2, 1],
    [5, 4, 3, 2, 1],
    [3, 4, 6, 2, 1, 5],
    [4, 1, 3, 5, 6, 2],
    [2, 6, 4, 1, 3, 5],
    [8, 6, 4, 2, 3, 5, 7, 1]
]:
    main(nums)
    print(nums)
