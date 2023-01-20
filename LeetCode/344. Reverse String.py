from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


if __name__ == '__main__':
    # Test Case 1
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)  # ["o", "l", "l", "e", "h"]

    # Test Case 2
    s = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(s)
    print(s)  # ["h","a","n","n","a","H"]
