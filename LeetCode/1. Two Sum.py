class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            if target - n in nums[i + 1:]:
                return [i, i + 1 + nums[i + 1:].index(target - n)]
