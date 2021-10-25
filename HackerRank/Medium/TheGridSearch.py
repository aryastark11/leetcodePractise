#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#


# worst Case when --> 111111111, 111111111, 111101111
# and pattern is  ---> 1111, 1111, 1110
# gotta check all combinations of 1111 -> startIndx=0,1,2,3,4,5

def find_all(string, substring):
    index = []
    L = len(string)
    l = len(substring)
    for i in range(0, L-l+1):
        if string[i:i+l] == substring:
            index.append(i)
    return index

def gridSearch(G, P):
    # Write your code here
    ii = 0
    listFirstPattern = []
    firstPattern = P[0]
    findingJJ = []
    while(ii < (len(G)-len(P)+1)):
        if(G[ii].count(firstPattern)):
            # get startIndex of all occurances of P[0] in G[ii]
            listFirstPattern = find_all((G[ii]), firstPattern)

            addRes = 1
            dictCommonIndices = listFirstPattern
            # check occurances of P[1:] in G[ii:]

            for jj in range(1, len(P)):
                if(G[ii+jj].count(P[jj])):
                    findingJJ = find_all((G[ii+jj]), P[jj])
                    # for all strings in P[1:x] pattern start index is a subset or fully
                    # matches the indices of P[0]. 
                    # condition is that it should be same index.
                    # so iteratively check the start index intersection.
                    print(dictCommonIndices)
                    print("findingJJ : {}".format(findingJJ))
                    # check intersection of indices.
                    if (set(findingJJ)&set(dictCommonIndices)):
                        dictCommonIndices = list(set(findingJJ)&set(dictCommonIndices))
                        addRes += 1
                    else:
                        break
                else:
                    break
            listFirstPattern = []
            findingJJ = []
            if addRes == len(P):
                return "YES"
        ii = ii+1
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()