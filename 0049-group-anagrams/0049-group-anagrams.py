class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freq = {}
        for i in strs:
         
           key = "".join(sorted(i))
           if key not in freq:
               freq[key] = []

           freq[key].append(i)
    
        return freq.values()