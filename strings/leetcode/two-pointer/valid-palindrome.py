inputs = [
    [1, 2, 2, 1]
]


def main(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        if nums[low] != nums[high]:
            return False
        low, high = low + 1, high - 1
    return True


for input in inputs:
    print(main(input))
