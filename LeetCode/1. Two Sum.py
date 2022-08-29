class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for idx in range(len(nums) - 1):
            if target - nums[idx] in nums[idx + 1:]:
                return [idx, idx + nums[idx + 1:].index(target - nums[idx]) + 1]
