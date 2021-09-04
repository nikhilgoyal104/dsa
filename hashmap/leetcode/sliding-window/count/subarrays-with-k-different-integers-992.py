from collections import Counter


# T=n,S=1
def main(nums, k):
    def atMost(k):
        res, n = 0, len(nums)
        freq, j = Counter(), 0
        for i in range(n):
            freq[nums[i]] += 1
            while len(freq) > k:
                freq[nums[j]] -= 1
                if not freq[nums[j]]:
                    del freq[nums[j]]
                j += 1
            res += (i - j + 1)
        return res

    return atMost(k) - atMost(k - 1)


for nums, k in [
    ([1, 2, 1, 2, 3], 2),
    ([1, 2, 1, 3, 4], 3)
]:
    print(main(nums, k))
