class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * 1 if n % 2 == 0 else n * 2
