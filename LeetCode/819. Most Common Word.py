import re
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return [word for word in list(map(lambda x: x[0], sorted(
            Counter(map(lambda x: x.lower(), re.compile(r'[A-Za-z]+').findall(paragraph))).items(), key=lambda x: x[1],
            reverse=True))) if word not in banned][0]
