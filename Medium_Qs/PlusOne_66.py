class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stri = ""
        for node in digits:
            stri += str(node)
        retVal = str(int(stri) + 1)
        retList = []
        for node in retVal:
            retList.append(int(node))
        return retList
		
## ======================================================================================================
# optimized solution

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        flag=0
        n=n-1
        while n>=0:
            if digits[n]<9:
                digits[n]=digits[n]+1
                flag=1
                return digits
            else:
                digits[n]=0
            n=n-1
        if flag==0:
            digits.insert(0,1)
            return digits