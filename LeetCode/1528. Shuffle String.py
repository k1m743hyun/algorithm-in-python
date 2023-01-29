from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([v for k, v in sorted({indices[i]: s[i] for i in range(len(s))}.items())])


if __name__ == '__main__':
    # Test Case 1
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    print(Solution().restoreString(s, indices))  # leetcode

    # Test Case 2
    s = "abc"
    indices = [0, 1, 2]
    print(Solution().restoreString(s, indices))  # abc
