# T=nlogn,S=n
def main(nums):
    time = []
    for start, end in nums:
        time.append((start, 1))
        time.append((end, -1))
    time.sort()
    count = res = 0
    for _, room in time:
        count += room
        res = max(res, count)
    return res


for nums in [
    [[0, 30], [5, 10], [15, 20]],
    [[7, 10], [2, 4]],
    [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
]:
    print(main(nums))
