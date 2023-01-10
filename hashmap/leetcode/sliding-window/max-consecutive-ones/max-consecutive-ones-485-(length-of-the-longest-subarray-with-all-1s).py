# T=n,S=1
def main(nums):
    res = count = 0
    for val in nums:
        if val:
            count += 1
        else:
            res = max(res, count)
            count = 0
    return max(res, count)


for nums in [
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 0, 0],
    [0],
    [1],
]:
    print(main(nums), end=' ')
