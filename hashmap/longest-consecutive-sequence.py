# T=n,S=n
def main(nums):
    aset, msize, mseq = set(nums), 0, []
    for val in nums:
        if val - 1 not in aset:
            size, seq = 1, [val]
            while val + 1 in aset:
                size += 1
                val += 1
                seq.append(val)
            if size > msize:
                msize, mseq = size, seq
    print(mseq, msize)


for nums in [
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    [10, 5, 9, 1, 11, 8, 6, 15, 3, 12, 2]
]:
    main(nums)
