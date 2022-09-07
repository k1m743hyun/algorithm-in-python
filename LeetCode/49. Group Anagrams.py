from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for s in strs:
            results[''.join(sorted(s))].append(s)

        return results.values()
