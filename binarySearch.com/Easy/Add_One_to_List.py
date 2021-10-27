class Solution:
    def solve(self, nums):
        number = [str(i) for i in nums]
        number = ''.join(number)
        number = int(int(number) + 1)
        print(number)
        return [int(i) for i in str(number)]


### optimised solution
### 1 liner
  return list(map(int, str(int("".join(map(str, nums))) + 1)))
