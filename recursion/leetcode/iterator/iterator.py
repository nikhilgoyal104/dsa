from typing import List


class Iterator:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(nums)
