from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {v: [] for v in set([''.join(sorted(s)) for s in strs])}
        for s in strs:
            results[''.join(sorted(s))].append(s)
        return sorted(map(lambda x: sorted(x), results.values()), key=lambda x: len(x))
