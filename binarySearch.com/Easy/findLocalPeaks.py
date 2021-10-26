class Solution:
    def solve(self, nums):
        asd = []
        if len(nums) < 2:
            return asd
        
        for ii in range(0, len(nums)):
            if ii ==0:
                if nums[ii] > nums[ii+1]:
                    asd.append(ii)
            elif ii == len(nums)-1:
                if nums[ii] > nums[ii-1]:
                    asd.append(ii)
            else:
                if nums[ii] > nums[ii-1] and nums[ii] > nums[ii+1]:
                    asd.append(ii)
        return asd
