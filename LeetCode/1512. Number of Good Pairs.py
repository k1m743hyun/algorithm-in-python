from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([1 for j in range(len(nums)) for i in range(len(nums)) if i < j and nums[i] == nums[j]])


if __name__ == '__main__':
    # Test Case 1
    nums = [1, 2, 3, 1, 1, 3]
    print(Solution().numIdenticalPairs(nums))  # 4

    # Test Case 2
    nums = [1, 1, 1, 1]
    print(Solution().numIdenticalPairs(nums))  # 6

    # Test Case 3
    nums = [1, 2, 3]
    print(Solution().numIdenticalPairs(nums))  # 0
