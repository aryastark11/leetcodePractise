class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or not nums or k <= 0:
            return False
        buckets = {}
        width = t + 1

        for n, i in enumerate(nums):
            buck = i // width
            if buck in buckets:
                return True
            else:
                buckets[buck] = i
                if buck - 1 in buckets and i - buckets[buck-1] <= t:
                    return True
                if buck + 1 in buckets and buckets[buck+1] - i <= t:
                    return True
                if n >= k:
                    del buckets[nums[n-k] // width]
        return False


#### optimised solution

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        l1, l2 = sorted(nums), sorted(range(len(nums)), key=lambda i: nums[i])
        
        ## l2 is the list of indices of elements in the l1 in actual list nums
        # nums = [1,2,3,1]
        # l1 = [1,1,2,3]  # sorted order of nums
        # l2 = [0, 3, 1, 2] # indices of 1,1,2,3 in nums
        
        i = 0
        j = 1
                        
        while j < len(l2):
            diff = l1[j] - l1[i]
            if diff <= t:
                if abs(l2[j] - l2[i]) <= k:
                    return True
                j+=1  # issue with index, find the next index, such that the difference in
                      # nums[i] is still <=t
            else:
                i+=1  # next element in the array
                j = i + 1  # next element in the list
        
        return False        
