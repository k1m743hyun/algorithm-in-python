from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for idx, val in enumerate(candies):
            candies[idx] = val + extraCandies
            if max(candies) <= val + extraCandies:
                result.append(True)
            else:
                result.append(False)
            candies[idx] = val
        return result
      