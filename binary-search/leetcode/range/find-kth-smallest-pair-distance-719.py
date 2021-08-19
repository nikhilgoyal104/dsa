from heapq import *


# T=n²log(n²)
def w(nums, k):
    pairs = [[nums[i], nums[j]] for i in range(len(nums)) for j in range(i + 1, len(nums))]
    pairs.sort(key=lambda x: abs(x[0] - x[1]))
    return abs(pairs[k - 1][0] - pairs[k - 1][1])


# T=n²logk
def x(nums, k):
    heap = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            heappush(heap, -abs(nums[i] - nums[j]))
            if len(heap) > k:
                heappop(heap)
    return -heappop(heap)


# T=(nlogn)+(n+klogn)=n+(n+k)logn,S=n
def y(nums, k):
    res, heap, n = None, [], len(nums)
    nums = sorted(nums)
    for i in range(n - 1):
        ri, ci = i, i + 1
        heap.append((abs(nums[ci] - nums[ri]), ri, ci))
    heapify(heap)
    for _ in range(k):
        res, ri, ci = heappop(heap)
        if ci + 1 < n:
            heappush(heap, (abs(nums[ci + 1] - nums[ri]), ri, ci + 1))
    return res


# T=nlogn+log(w)n
def z(nums, k):
    def count(mid):
        n, count, j = len(nums), 0, 1
        for i in range(n - 1):
            while j < n and (nums[j] - nums[i]) <= mid:
                j += 1
            count += j - i - 1
        return count

    nums.sort()
    low, high = min(nums[i + 1] - nums[i] for i in range(len(nums) - 1)), max(nums) - min(nums)
    while low <= high:
        mid = low + (high - low) // 2
        if count(mid) >= k:
            high = mid - 1
        else:
            low = mid + 1
    return low


# 1<=k<=n(n-1)/2
for nums, k in [
    ([1, 3, 1], 1),
    ([1, 1, 1], 2),
    ([1, 6, 1], 3),
    ([2, 2, 0, 1, 1, 0, 0, 1, 2, 0], 2),
    ([9, 10, 7, 10, 6, 1, 5, 4, 9, 8], 18),
    ([2, 4, 5, 8, 9], 5)
]:
    print(w(nums, k), end=' ')
    print(x(nums, k), end=' ')
    print(y(nums, k), end=' ')
    print(z(nums, k))
