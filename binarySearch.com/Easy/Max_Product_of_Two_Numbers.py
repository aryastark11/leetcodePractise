class Solution:
    def solve(self, nums):
        # 5,1,7 --> 35
        # -10, -8, 1, 2 --> 80
        # -10, 1, 100 --> 100
        # -100, -100, -100, -1, 0 --> 100
        # -2, 3 --> -6
        # 0,0 --> 0
        # sort the set in ascending order
        sortNums = sorted(nums)
        # assuming all positive and taking last two largest elements
        maxProd = sortNums[-1] * sortNums[-2]

        maxProdNeg = -1 * pow(10, 10)
        if sortNums[0] < 0 and sortNums[1] < 0:
            maxProdNeg = abs(sortNums[0]) * abs(sortNums[1])
        
        return max(maxProd, maxProdNeg)
        
        
        
## optmised solution
"""
        ## max(largest*second_largest, smallest*second_smallest)
        copy = nums.copy()
        largest, smallest = max(nums), min(copy)
        nums.remove(largest), copy.remove(smallest)
        second_largest, second_smallest = max(nums), min(copy)

        return max(largest * second_largest, smallest * second_smallest)
"""


"""
class Solution:
    def solve(self, nums):
        # 5,1,7 --> 35
        # -10, -8, 1, 2 --> 80
        # -10, 1, 100 --> 100
        # -100, -100, -100, -1, 0 --> 100
        # -2, 3 --> -6
        # 0,0 --> 0
        # sort the set in ascending order
        asd = sorted(nums)
        leftProd = asd[0] * asd[1]
        rightProd = asd[-1] * asd[-2]
        return max(leftProd, rightProd)
"""        
        
