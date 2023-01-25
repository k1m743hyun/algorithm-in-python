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


if __name__ == '__main__':
    # Test Case 1
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(Solution().kidsWithCandies(candies, extraCandies))  # [true, false, false, false, false]

    # Test Case 2
    candies = [12, 1, 12]
    extraCandies = 10
    print(Solution().kidsWithCandies(candies, extraCandies))  # [true, false, true]
