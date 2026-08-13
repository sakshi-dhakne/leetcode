class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1,-1]

        n = len(nums)
        low = 0
        high = n-1
        lower_bound = n

        # lower bound
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=target:
                lower_bound = mid
                high = mid-1
            else:
                low = mid+1
        
        # upper bound
        upper_bound = n
        n = len(nums)
        low = 0
        high = n-1        
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>target:
                upper_bound = mid
                high = mid-1
            else:
                low = mid+1
        
        if lower_bound == n or nums[lower_bound]!=target:
            return [-1,-1]
        
        return [lower_bound,upper_bound-1]
             