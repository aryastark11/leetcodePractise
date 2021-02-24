class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) ==0:
            return True
        i = 1
        s = A[1:] + A[0]
        while(i< len(A)):
            if s == B:
                return True
            s = s[1:] + s[0]
            i += 1

        return False

## ======================================================================================================
# optimized solution
		
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A		