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
