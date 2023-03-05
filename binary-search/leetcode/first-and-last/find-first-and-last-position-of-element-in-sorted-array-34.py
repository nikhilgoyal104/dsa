# T=logn,S=1
def main(nums, target):
    def getFirstPosition():
        res = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                res = mid
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return res

    def getLastPosition():
        res = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                res = mid
                low = mid + 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return res

    firstPosition = getFirstPosition()
    if firstPosition == -1:
        return [-1, -1]
    return [firstPosition, getLastPosition()]


for nums, target in [
    ([5, 7, 7, 8, 8, 10], 8),
    ([5, 7, 7, 8, 8, 10], 6),
    ([], 0)
]:
    print(main(nums, target))
