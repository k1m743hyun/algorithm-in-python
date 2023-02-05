from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


if __name__ == '__main__':
    # Test Case 1
    nums = [0, 2, 1, 5, 3, 4]
    print(Solution().buildArray(nums))  # [0, 1, 2, 4, 5, 3]

    # Test Case 2
    nums = [5, 0, 1, 2, 3, 4]
    print(Solution().buildArray(nums))  # [4, 5, 0, 1, 2, 3]
