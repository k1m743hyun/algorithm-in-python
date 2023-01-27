from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        result = []
        for n in nums:
            s += n
            result.append(s)

        return result


if __name__ == '__main__':
    # Test Case 1
    nums = [1, 2, 3, 4]
    print(Solution().runningSum(nums))  # [1, 3, 6, 10]

    # Test Case 2
    nums = [1, 1, 1, 1, 1]
    print(Solution().runningSum(nums))  # [1,2,3,4,5]

    # Test Case 3
    nums = [3, 1, 2, 10, 1]
    print(Solution().runningSum(nums))  # [3,4,6,16,17]
