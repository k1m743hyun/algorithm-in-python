from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([1 for j in range(len(nums)) for i in range(len(nums)) if i < j and nums[i] == nums[j]])
