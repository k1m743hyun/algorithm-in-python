class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([1 for stone in stones for jewel in jewels if jewel == stone])


if __name__ == '__main__':
    # Test Case 1
    jewels = "aA"
    stones = "aAAbbbb"
    print(Solution().numJewelsInStones(jewels, stones))  # 3

    # Test Case 2
    jewels = "z"
    stones = "ZZ"
    print(Solution().numJewelsInStones(jewels, stones))  # 0
