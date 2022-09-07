import re
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return Counter([word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]).most_common(1)[0][0]
