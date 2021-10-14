# T=nlogn,S=n
def main(nums):
    nums.sort()
    res = []
    for val in nums:
        if not res or res[-1][1] < val[0]:
            res.append(val)
        else:
            res[-1][1] = max(res[-1][1], val[1])
    return res


for nums in [
    [[1, 3], [2, 6], [8, 10], [15, 18]],
    [[1, 4], [4, 5]],
    [[1, 3], [2, 4], [5, 7], [6, 8]],
    [[1, 4], [2, 3]],
    [[10, 16], [2, 8], [1, 6], [7, 12]],
    [[1, 2], [2, 3], [3, 4], [1, 3]]
]:
    print(main(nums), end='')
    print()
