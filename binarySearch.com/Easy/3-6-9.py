class Solution:
    def solve(self, n):

        list1 = []
        str1 = "clap"
        str2 = "369"
        for i in range(1, n+1):
            if i%3 == 0:  ## multiple of 3
                list1.append(str1)
            elif (set(str(i)) & set(str2)):  ## has 3,6,9 in the number
                ## check if set(number) contains 3,6 or 9
                list1.append(str1)
            else:
                list1.append(str(i))
        return list1

## optimised solution
        """
        def valid(x):
            if x % 3 == 0:
                return False
            while x:
                if x % 10 in [3, 6, 9]:
                    return False
                x //= 10
            return True 

        return [str(i) if valid(i) else "clap" for i in range(1, n + 1)]
        """
