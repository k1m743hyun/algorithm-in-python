from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for idx in range(len(encoded)):
            arr.append(arr[idx] ^ encoded[idx])
        return arr
