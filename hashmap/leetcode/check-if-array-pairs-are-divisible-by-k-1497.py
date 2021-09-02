from collections import Counter


# T=n,S=n
def main(nums, k):
    freq = Counter()
    for val in nums:
        freq[val % k] += 1
    if freq[0] % 2:
        return False
    for rem in freq:
        if rem and freq[rem] != freq[k - rem]:
            return False
    return True


for nums, k in [
    ([11, 17, 13, 18], 10),
    ([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5),
    ([1, 2, 3, 4, 5, 6], 7),
    ([1, 2, 3, 4, 5, 6], 10),
    ([-10, 10], 2),
    ([-1, 1, -2, 2, -3, 3, -4, 4], 3),
    ([1, 1, 1, 1, 1, 1], 6),
]:
    print(main(nums, k))
