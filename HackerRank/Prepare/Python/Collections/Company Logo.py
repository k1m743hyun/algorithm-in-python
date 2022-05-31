#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    
    for k, v in sorted(sorted(Counter(s).items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)[:3]:
        print(k, v)
