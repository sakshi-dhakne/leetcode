class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        freq = {}
        for index,current in enumerate(nums):
            if current in freq :
                print(freq[current],index)
                a = index
                b = freq[current]
                if (a-b) <= k:
                    return True
            freq[current] = index
            
        else:
            return False

            