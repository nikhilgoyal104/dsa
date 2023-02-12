# T=n²,S=1
def main(nums):
    n = len(nums)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums


for nums in [
    [1, 2, 3, 4, 5],
    [64, 25, 12, 22, 11],
    [5, 4, 3, 2, 1]
]:
    print(main(nums))
