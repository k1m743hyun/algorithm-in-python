from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


if __name__ == '__main__':
    # Test Case 1
    nums = [1, 2, 1]
    print(Solution().getConcatenation(nums))  # [1, 2, 1, 1, 2, 1]

    # Test Case 2
    nums = [1, 3, 2, 1]
    print(Solution().getConcatenation(nums))  # [1, 3, 2, 1, 1, 3, 2, 1]
