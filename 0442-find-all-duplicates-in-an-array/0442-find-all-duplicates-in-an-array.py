class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        result = []

        for i in nums:
            freq[i] = freq.get(i,0)+1
            if freq[i] == 2:
                result.append(i)

        return (result)