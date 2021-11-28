# T=logn,S=1
def main(nums, target):
    def first():
        low, high, res = 0, len(nums) - 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target <= nums[mid]:
                high = mid - 1
            else:
                res, high = mid, mid - 1
        return res

    def last():
        low, high, res = 0, len(nums) - 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                res, low = mid, mid + 1
        return res

    f = first()
    return [-1, -1] if f == -1 else [f, last()]


for nums, target in [
    ([5, 7, 7, 8, 8, 10], 8),
    ([5, 7, 7, 8, 8, 10], 6),
    ([], 0)
]:
    print(main(nums, target))
