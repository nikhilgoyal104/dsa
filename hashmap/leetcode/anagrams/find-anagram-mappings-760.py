from collections import defaultdict, deque


# T=n,S=n
def main(nums1, nums2):
    res, mapping = [], defaultdict(deque)
    for i, v in enumerate(nums2):
        mapping[v].append(i)
    return [mapping[val].popleft() for val in nums1]


for nums1, nums2 in [
    ([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]),
    ([84, 46], [84, 46]),
    ([12, 28, 46], [46, 12, 28]),
    ([2, 7, 9, 2, 8, 1, 1, 3, 9], [3, 1, 2, 9, 8, 1, 7, 9, 2])
]:
    print(main(nums1, nums2))
