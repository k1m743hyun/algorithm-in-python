#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    # return Counter(s * (n // len(s)) + s[:n % len(s)])['a']
    return Counter(s)['a'] * (n // len(s)) + Counter(s[:n % len(s)])['a']


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
