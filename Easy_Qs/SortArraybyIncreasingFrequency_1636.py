class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mapDict = {}
        resList = []
        nums.sort(reverse=True)
        for node in nums:
            mapDict.update({node: nums.count(node)})
        sortedDict = sorted(mapDict.items(), key=operator.itemgetter(1))
        # check if there are elements with same freq           
        
        for key,val in sortedDict:                
                resList.extend([key]*val)
        return resList
     
     
class OptimisedSolution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqMap = collections.Counter(nums)
        res = []
        for num, count in sorted(freqMap.items(), key=lambda x : (x[1], -x[0])):
            for i in range(count):
                res.append(num)
        return res