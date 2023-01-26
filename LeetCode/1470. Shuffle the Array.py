from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]

        result = []
        for i in range(n):
            result.append(x[i])
            result.append(y[i])

        return result


if __name__ == '__main__':
    # Test Case 1
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(Solution().shuffle(nums, n))  # [2, 3, 5, 4, 1, 7]

    # Test Case 2
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    print(Solution().shuffle(nums, n))  # [1,4,2,3,3,2,4,1]

    # Test Case 3
    nums = [1, 1, 2, 2]
    n = 2
    print(Solution().shuffle(nums, n))  # [1,2,1,2]
