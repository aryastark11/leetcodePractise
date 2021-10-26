class Solution:
    def solve(self, s0, s1):
        # s0 = Hello hello hEllo
        # s1 = hello HELLO hello

        # convert all characters of s0 and s1 to lowerCase.
        # for easy comparison
        # then remove duplicates by using set
        # then get intersection.
        s0Set = set(s0.lower().split())
        s1Set = set(s1.lower().split())
        return len(list(s0Set & s1Set))
