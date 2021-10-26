class Solution:
    def solve(self, n, a, b):
        # line is 1,2,3,4,5,6,7,8,9,10, ... n
        # sample input n = 10, a = 3, b = 4
        
        # atleast 3 in front --> so start from 4,5, 6,7,8,9,10
        frontPos = a+1
        
        # atmost 4 behind --> so start from 6,7,8,9,10
        backPos = n-b

        # rightStartPosition --> maximum of these two 
        # max(4,6) = 6
        rightStart = max(frontPos, backPos)
        
        # all possible positions --> 6,7,8,9,10 --> 5 in number
        return n-rightStart+1        


## submission results
"""
Success!
Your code took 1 millisecond — faster than 100.00% in Python
"""
