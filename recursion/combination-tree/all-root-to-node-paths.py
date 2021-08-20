def x(nums, i, start, path):
    if i != -1:
        path.append(nums[i])
    print(path, end=' ')
    for i in range(start, len(nums)):
        x(nums, i, i + 1, path)
    if path:
        path.pop()


def y(nums, start, path):
    print(path, end=' ')
    for i in range(start, len(nums)):
        y(nums, i + 1, path + [nums[i]])


for nums in [
    [1, 2, 3],
    [1, 2, 3, 4]
]:
    x(nums, -1, 0, [])
    print()
    y(nums, 0, [])
    print()
