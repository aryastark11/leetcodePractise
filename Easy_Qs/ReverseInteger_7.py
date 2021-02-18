class Solution:
    def reverse(self, x: int) -> int:
        # take the absolute value and convert it to string
        # and reverse it and convert back to int
        y = int(str(abs(x))[::-1])
        # convert it to -ve, if original no. is -ve
        y = y * (-1 if x < 0 else 1)
        # return only if reversed int falls under int range.
        return (y if -2**31  <= y <= 2**31 -1 else 0)