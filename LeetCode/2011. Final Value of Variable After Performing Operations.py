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
      