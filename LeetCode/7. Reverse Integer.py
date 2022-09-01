class Solution:
    def reverse(self, x: int) -> int:
        nx = int(str(x)[:0:-1]) * -1 if x < 0 else int(str(x)[::-1])
        return nx if -(2 ** 31) < nx < (2 ** 31) - 1 else 0
