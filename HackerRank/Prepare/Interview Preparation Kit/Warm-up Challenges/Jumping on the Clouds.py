#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    result = []
    for i, v in enumerate(c):
        if i == 0:
            result.append(v)
        else:
            if i < len(c) - 1:
                if c[i - 1] == c[i] == c[i + 1]:
                    c[i] = 1
                    result.append(1)
                elif c[i - 1] == c[i]:
                    result.append(1)
                    result.append(v)
                else:
                    result.append(v)
            else:
                if c[i - 1] == c[i]:
                    result.append(1)
                    result.append(v)
                else:
                    result.append(v)

    return sum(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
