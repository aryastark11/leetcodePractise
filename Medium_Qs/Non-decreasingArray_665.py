class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        pivot = []  # list to hold indices of elements that are out of order
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:  # in ascending order 2,4
                try:
                    # order is same -> 2,4,6
                    if nums[i+1] > nums[i-1]:
                        pivot.append(i)
                    else:  # order is messed up -> 2,4,1 or 2,4,2
                        pivot.append(i-1)
                except:  # handle last element --> out of index error in list
                    pivot.append(i)
        print(pivot)
        if len(pivot) > 1:
            return False
        if len(pivot) < 1:
            if nums == sorted(nums):
                return True
            return False
        # when pivot has only one element
        try:
            nums[pivot[0]] = nums[pivot[0]+1]
        except:
            nums[pivot[0]] = nums[pivot[0]-1]
        if nums ==  sorted(nums):
            return True
        return False

		
		
#### optimised solution

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        # count=0
        # for i in range(len(nums)-1):
        #     if nums[i]>nums[i+1]:
        #         count+=1
        #         if count>1 or ((i-1>=0 and nums[i-1]>nums[i+1]) and (i+2<len(nums) and nums[i+2]<nums[i])):
        #             return False
        # return True
        count = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
                if count>1 or ((i-1>=0 and nums[i-1]>nums[i+1]) and (i+2<len(nums) and nums[i+2]<nums[i])):
                    return False
        return True		
