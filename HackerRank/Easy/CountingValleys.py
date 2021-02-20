#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    mapDict = {'U': 1, 'D': -1}
    intCount = 0
    retInt = []
    for e in path:
        intCount += mapDict[e]
        if intCount == 0:
            retInt.append(e)
    if 'U' in retInt:
        return retInt.count('U')
    return 0     
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()