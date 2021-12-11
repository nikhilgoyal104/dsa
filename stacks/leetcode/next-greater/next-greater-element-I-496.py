# T=n,S=n
def main(nums1, nums2):
    stack, map = [], {}
    for val in nums2:
        while stack and stack[-1] < val:
            map[stack.pop()] = val
        stack.append(val)
    return [map.get(val, -1) for val in nums1]


for nums1, nums2 in [
    ([4, 1, 2], [1, 3, 4, 2]),
    ([2, 4], [1, 2, 3, 4])
]:
    print(main(nums1, nums2))
