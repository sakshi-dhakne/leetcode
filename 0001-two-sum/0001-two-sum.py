class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        for index,current in enumerate(nums):
            i = target - current
            if i not in seen:
                seen[current] = index
            else :
                return(seen[i],index)
        