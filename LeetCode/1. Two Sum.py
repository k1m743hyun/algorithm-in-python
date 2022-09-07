from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for idx, num in enumerate(nums):
            if target - num in nums_dict:
                return [idx, nums_dict[target - num]]
            nums_dict[num] = idx
