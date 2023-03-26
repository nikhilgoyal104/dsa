# T=n,S=n
def main(nums):
    numsSet = set(nums)
    maxSize = 0
    longestConsecutiveSeq = []
    for val in nums:
        if val - 1 not in numsSet:
            size = 1
            seq = [val]
            while val + 1 in numsSet:
                val += 1
                size += 1
                seq.append(val)
            if size > maxSize:
                maxSize = size
                longestConsecutiveSeq = seq
    print(longestConsecutiveSeq, maxSize)


for nums in [
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    [10, 5, 9, 1, 11, 8, 6, 15, 3, 12, 2]
]:
    main(nums)
