class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return nums[0]
        curr = 0
        best = nums[0]
        for i in range(len(nums)):
            curr += nums[i]

            if curr > best:
                best = curr
            if curr < 0:
                curr = 0
        
        return best