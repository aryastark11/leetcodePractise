import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        Quo = 0
        Neg = True
        posRange = 2**31 -1
        negRange = -(2**31)
        if abs(dividend) < abs(divisor):
            return Quo
        if dividend<0 and divisor< 0 or (dividend>0 and divisor>0):
            Neg = False
        if abs(divisor) == abs(dividend):
            return 1*(-1 if Neg else 1)
        if abs(divisor) == 1:
            Quo = abs(dividend) *(-1 if Neg else 1)

        else:
            # divide using logarithm
            # refer https://sciencing.com/use-log-ti83-8272011.html
            dvd = math.log(abs(dividend), 10)
            dvs = math.log(abs(divisor), 10)
            Quo = 10**(dvd-dvs) * (-1 if Neg else 1)
            print(dvd-dvs)
        print(Quo)
        # to handle rounding off part, only if it is .99999 and terminates to 0, round to next number, else remove the decimal part. 
        if abs(Quo) - abs(math.trunc(Quo)) > 0.99999:
            Quo = round(Quo)
        print(Quo)
        print(negRange)
        print(posRange)

        if Quo > posRange:
            return posRange 
        if Quo < negRange:
            return negRange
        return int(Quo)
		
		
## optimised solution

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res, flag = 0, 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            flag = -1
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            n = 0
            while dividend >= divisor << n:
                n += 1
            res += 1 << (n - 1)    ## using left and right shift
            dividend -= (divisor << (n-1))
        res = -res if flag == -1 else res
        if res < -2147483648 or res > 2147483647:
            return 2147483647
        return res