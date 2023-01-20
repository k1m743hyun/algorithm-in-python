from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for s in strs:
            results[''.join(sorted(s))].append(s)

        return results.values()


if __name__ == '__main__':
    # Test Case 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))  # [["bat"],["nat","tan"],["ate","eat","tea"]]

    # Test Case 2
    strs = [""]
    print(Solution().groupAnagrams(strs))  # [[""]]

    # Test Case 3
    strs = ["a"]
    print(Solution().groupAnagrams(strs))  # [["a"]]
