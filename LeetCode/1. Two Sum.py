from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, num in enumerate(nums):
            if target - num in nums_dict:
                return [idx, nums_dict[target - num]]
            nums_dict[num] = idx


if __name__ == '__main__':
    # Test Case 1
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))  # [0, 1]

    # Test Case 2
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))  # [1, 2]

    # Test Case 3
    nums = [3, 3]
    target = 6
    print(Solution().twoSum(nums, target))  # [0, 1]
