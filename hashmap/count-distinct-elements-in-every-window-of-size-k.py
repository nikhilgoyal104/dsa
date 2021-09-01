from collections import defaultdict


# T=n,S=n
def main(nums, k):
    n, freq = len(nums), defaultdict(int)
    for i in range(k):
        freq[nums[i]] += 1
    res = [len(freq)]
    for i in range(k, n):
        outgoing, incoming = nums[i - k], nums[i]
        freq[outgoing] -= 1
        if not freq[outgoing]:
            del freq[outgoing]
        freq[incoming] += 1
        res.append(len(freq))
    return res


for nums, k in [
    ([1, 2, 1, 3, 4, 2, 3], 4),
    ([1, 2, 4, 4], 2),
    ([2, 5, 5, 6, 3, 2, 3, 2, 4, 5, 2, 2, 2, 2, 3, 6], 4)
]:
    print(main(nums, k))
