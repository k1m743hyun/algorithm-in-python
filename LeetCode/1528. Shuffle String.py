from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([v for k, v in sorted({indices[i]: s[i] for i in range(len(s))}.items())])
