

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        for i in p:
            # p = axb
            # s = abababa
            # some element in P is not there in S
            if i not in s:
                return -1

        count = 0
        existList = {}
        reducedDic = {}
        startIndex = 0
        endIndex = 0
        for ii in range(0, len(s)):
            if s[ii] in p:
                # fresh new element
                if s[ii] not in existList.keys():
                    count = count + 1
                existList.update({s[ii]: ii})
                
            if count == len(p):
                startIndex = min(existList.values())
                endIndex = ii
                # to store start and end index.
                soln = endIndex - startIndex + 1
                count = 0
                existList = {}
                # if strLength of 4 is not present, add it
                # if strLength of 4 is present, dont change, as the one with
                # least index, already exists (we are going from 0 --> n)
                if soln not in reducedDic:
                    asd = [startIndex, endIndex]
                    reducedDic.update({soln: asd})
        
        keyList = sorted(reducedDic.keys())
        #print(existList)
        #print(reducedDic)
        #print(reducedDic[keyList[0]])
        try:
            asd = s[reducedDic[keyList[0]][0]: reducedDic[keyList[0]][1]+1]
            return asd
        except Exception:
            #print(reducedDic)
            return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends