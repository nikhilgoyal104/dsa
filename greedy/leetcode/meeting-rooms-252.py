inputs = [
    [[0, 30], [5, 10], [15, 20]],
    [[7, 10], [2, 4]]
]


def overlap(i1, i2):
    return min(i1[1], i2[1]) > max(i1[0], i2[0])


# T=n²,S=1
def main(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if overlap(nums[i], nums[j]):
                return False
    return True


for nums in inputs:
    print(main(nums))

print()


# T=nlogn,S=n
def main(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        endTimeOfCurrentMeeting = nums[i][1]
        startTimeOfNextMeeting = nums[i + 1][0]
        if endTimeOfCurrentMeeting > startTimeOfNextMeeting:
            return False
    return True


for nums in inputs:
    print(main(nums))
