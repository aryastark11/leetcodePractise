class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        pivot = []
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                try:
                    if nums[i+1] > nums[i-1]:
                        pivot.append(i)
                    else:
                        pivot.append(i-1)
                except:
                    pivot.append(i)
        print(pivot)
        if len(pivot) > 1:
            return False
        if len(pivot) < 1:
            if nums == sorted(nums):
                return True
            return False
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