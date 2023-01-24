from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i, v in enumerate(nums):
            cnt = 0
            for j, n in enumerate(nums):
                if j != i and n < v:
                    cnt += 1
            result.append(cnt)
        return result


if __name__ == '__main__':
    # Test Case 1
    nums = [6, 5, 4, 8]
    print(Solution().smallerNumbersThanCurrent(nums))  # [2, 1, 0, 3]

    # Test Case 2
    nums = [7, 7, 7, 7]
    print(Solution().smallerNumbersThanCurrent(nums))  # [0, 0, 0, 0]
