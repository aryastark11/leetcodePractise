class Solution:
    def solve(self, num):
        ## get the reverse of the number and compare
        """ 
    set1 = []
    num3 = num
    num2 = 0
    while num3 > 0:
        set1.append(int(num3%10))
        num3 = int(num3/10)
    print(set1)
    set1.reverse()
    num2 = 0
    index = 0
    for i in set1:
        x = 10**(index)
        num2 = num2 + (x*i)
        index +=1 
    print(num2)
    if num == num2:
        return True
    return False
        """


# optimal solution
## instead of reversing full, reverse just half and compare

        if num < 0 or (num%10==0 and num!=0):
            return False
        rev = 0
        while num > rev:
            rev = int((rev*10)) + int(num%10)
            num = int(num/10)
        print(rev)
        print(num)
        if int(rev) == int(num) or int(rev/10) == int(num):
            return True
        return False
