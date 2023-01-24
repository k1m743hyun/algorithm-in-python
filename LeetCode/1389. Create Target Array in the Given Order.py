from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        return result


if __name__ == '__main__':
    # Test Case 1
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    print(Solution().createTargetArray(nums, index))  # [0, 4, 1, 3, 2]

    # Test Case 2
    nums = [1, 2, 3, 4, 0]
    index = [0, 1, 2, 3, 0]
    print(Solution().createTargetArray(nums, index))  # [0, 1, 2, 3, 4]
