class Solution:
    def solve(self, nums):
        answer = 0
        # gives {x: count of x in nums}
        # nums = [2, 3]
        # Counter({2: 1, 3: 1})

        c = Counter(nums)
        actualNums = list(c.keys())
        for jj in actualNums:
            # if jj+1 exists in nums
            # then take the count of the occurance.
            if c[jj + 1] > 0:
                answer += c[jj]
        return answer
