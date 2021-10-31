# T=n,S=1
def main(nums, n):
    if not n:
        return True
    size = len(nums)
    for i in range(size):
        if nums[i]:
            continue
        prev, next = 0 if not i else nums[i - 1], 0 if i == size - 1 else nums[i + 1]
        if not prev and not next:
            nums[i], n = 1, n - 1
        if not n:
            return True
    return False


for nums, n in [
    ([0, 0, 0, 0, 0, 1, 0, 0], 0),
    ([1, 0, 0, 0, 0, 1], 2),
    ([1, 0, 0, 0, 1, 0, 0], 2),
    ([0, 0, 1, 0, 1], 1),
    ([0, 0, 1, 0, 0], 1),
    ([0], 1),
]:
    print(main(nums, n))
