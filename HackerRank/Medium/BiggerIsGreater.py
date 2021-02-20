#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    returnStr = 'no answer'
    # already the largest
	if w == ''.join(sorted(w, reverse=True)):
        return returnStr
    # repetition of single char
	if len(set(w)) == 1:
        return returnStr


	# string = ABCFDDA 
	# here C string[2] is the pivot after which the order is broken
	# the next big element after C is D. search for D from backwards
	# first D is at string[-2]
	# replace C and D ie, at string[2] and string[-2] --> ABD | FD | C | A
	# now sort the chars after the pivot to form smallest change --> ABD | ACDF

	# find the pivot
    i = len(w) - 1
    while (i > 0 and w[i-1] >= w[i]):  # checking for descending order
        i -= 1
    
    # (pivot = i-1)
    # get the first element greater than pivot
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1

    returnStr = ''
    list1 = w[j] + w[i-1]
	# list1[0] is the newBigChar and list[1] -> pivot
    newStr = w[i:j] + list1[1] + w[j+1:]  # form a string after the pivot
	# sort the subString after replacing char
    # to form the nearest element after replacement
    returnStr = w[:i-1] + list1[0] + ''.join(sorted(newStr, reverse=False))
    return returnStr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
