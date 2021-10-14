from collections import Counter


# T=n,S=1
def main(nums, k):
    def atMost(k):
        res, n = 0, len(nums)
        freq, left = Counter(), 0
        for right in range(n):
            freq[nums[right]] += 1
            while len(freq) > k:
                freq[nums[left]] -= 1
                if not freq[nums[left]]:
                    del freq[nums[left]]
                left += 1
            res += (right - left + 1)
        return res

    return atMost(k) - atMost(k - 1)


for nums, k in [
    ([1, 2, 1, 2, 3], 2),
    ([1, 2, 1, 3, 4], 3)
]:
    print(main(nums, k))
