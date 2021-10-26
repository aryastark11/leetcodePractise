class Solution:
    def solve(self, s):
        asdStr = ""
        for ele in s:
            if ele == '(':
                asdStr +=  "("
            elif ele == ")":
                if asdStr:
                    asdStr = asdStr[:-1]
                else:
                    return False
        if len(asdStr):
            return False
        return True
