from math import inf


# T=nlogn
def main(nums):
    nums.sort(key=lambda x: x[1])
    res, prevEnd = [], -inf
    for i, (currStart, currEnd) in enumerate(nums):
        if currStart >= prevEnd:
            prevEnd = currEnd
            res.append(i)
    return res


for nums in [
    [[10, 20], [12, 25], [20, 30]],
    [[1, 2], [3, 4], [0, 6], [5, 7], [8, 9], [5, 9]],
]:
    print(main(nums), end='')
    print()
