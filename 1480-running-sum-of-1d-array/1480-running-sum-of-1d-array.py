class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        sum = 0
        for i in range(len(nums)):
            if (i-1)< 0 :
                ans = nums[i]
                sum = ans 
                result.append(ans)
            else:
                ans = nums[i]+sum
                sum = ans
                result.append(ans)

        return result