class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([1 for stone in stones for jewel in jewels if jewel == stone])
