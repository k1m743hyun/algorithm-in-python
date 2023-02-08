from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for o in operations:
            c = list(o)
            if c[0] == 'X':
                if c[1] == '+':
                    result += 1
                else:
                    result -= 1
            else:
                if c[0] == '+':
                    result += 1
                else:
                    result -= 1
            
        return result


if __name__ == '__main__':
    # Test Case 1
    operations = ["--X", "X++", "X++"]
    print(Solution().finalValueAfterOperations(operations)) # 1

    # Test Case 2
    operations = ["++X", "++X", "X++"]
    print(Solution().finalValueAfterOperations(operations)) # 3

    # Test Case 3
    operations = ["X++", "++X", "--X", "X--"]
    print(Solution().finalValueAfterOperations(operations)) # 0
      