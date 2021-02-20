#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the encryption function below.
def encryption(s):
    # remove all the spaces
    s = s.replace(" ", "")
    strLen = len(s)
    returnStr = ''
    listReq = [int(strLen ** 0.5), int(strLen ** 0.5) + 1]
    # to choose the lowest rows*cols value
    comb = [[listReq[0], listReq[0]],
            [listReq[1], listReq[1]],
            [listReq[0], listReq[1]]]
    rows = 0
    cols = 0
    for com in comb:
        if com[0]*com[1] > strLen:
            rows, cols = com[0], com[1]
        elif com[0]*com[1] == strLen:
            rows, cols = com[0], com[1]
            break

    if rows >= cols:
        iterLen = rows
    else:
        iterLen = rows+1
    for i in range(0, iterLen):
        for j in range(0, cols):
            try:
                returnStr += s[j*cols + i]
            except:
                break
        returnStr += ' '  # add space char after every sequence break
    return returnStr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
