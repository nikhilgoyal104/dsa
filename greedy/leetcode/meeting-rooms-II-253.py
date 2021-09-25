def main(nums):
    lst = []
    for start, end in nums:
        lst.append((start, 1))
        lst.append((end, -1))
    lst.sort()
    count = res = 0
    for pair in lst:
        count += pair[1]
        res = max(res, count)
    return res


for nums in [
    [[0, 30], [5, 10], [15, 20]],
    [[7, 10], [2, 4]],
    [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
]:
    print(main(nums))
