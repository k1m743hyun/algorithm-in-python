from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for idx in range(len(encoded)):
            arr.append(arr[idx] ^ encoded[idx])
        return arr


if __name__ == '__main__':
    # Test Case 1
    encoded = [1, 2, 3]
    first = 1
    print(Solution().decode(encoded, first)) # [1, 0, 2, 1]

    # Test Case 2
    encoded = [6,2,7,3]
    first = 4
    print(Solution().decode(encoded, first)) # [4, 2, 0, 7, 4]
