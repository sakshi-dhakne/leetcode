class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = set(nums)
        longest = 0

        for i in n :
            if (i-1) not in n:
                 current = i
                 length = 1
                 while (current+1) in n:
                    length += 1
                    current += 1 
                 if length > longest:
                    longest = length

        return longest