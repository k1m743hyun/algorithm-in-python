from __future__ import division

def average(array):
    # your code goes here
    s = set(array)
    return sum(s) / len(s)

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result