from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {val: idx for idx, val in enumerate(nums)}

        for idx, num in enumerate(nums):
            if target - num in nums_dict and idx != nums_dict[target - num]:
                return [idx, nums_dict[target - num]]
