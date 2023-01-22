from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for idx, val in enumerate(nums):
            if idx % 2 == 0:
                freq = val
            else:
                result += [val] * freq
        return result


if __name__ == '__main__':
    # Test Case 1
    nums = [1, 2, 3, 4]
    print(Solution().decompressRLElist(nums))  # [2, 4, 4, 4]

    # Test Case 2
    nums = [1, 1, 2, 3]
    print(Solution().decompressRLElist(nums))  # [1, 3, 3]
