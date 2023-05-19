def heapify(nums):
    for i in range((len(nums) // 2) - 1, -1, -1):
        _downheapify(i, nums)


def _downheapify(index, nums):
    n = len(nums)
    minIndex = index
    leftChildIndex = 2 * index + 1
    if leftChildIndex < n and nums[leftChildIndex] < nums[minIndex]:
        minIndex = leftChildIndex
    rightChildIndex = 2 * index + 2
    if rightChildIndex < n and nums[rightChildIndex] < nums[minIndex]:
        minIndex = rightChildIndex
    if minIndex != index:
        nums[index], nums[minIndex] = nums[minIndex], nums[index]
        _downheapify(minIndex, nums)


for nums in [
    [13, 3, 10, 4, 8, 5, 6, 9, 15, 17],
    [5, 4, 1, 2, 3]
]:
    print(nums)
    heapify(nums)
    print(nums)
    print(nums[0])
