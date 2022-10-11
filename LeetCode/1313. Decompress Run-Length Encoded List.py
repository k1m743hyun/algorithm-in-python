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
