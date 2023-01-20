import re
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return Counter([word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]).most_common(1)[0][0]


if __name__ == '__main__':
    # Test Case 1
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(Solution().mostCommonWord(paragraph, banned))  # ball

    # Test Case 2
    paragraph = "a."
    banned = []
    print(Solution().mostCommonWord(paragraph, banned))  # a
