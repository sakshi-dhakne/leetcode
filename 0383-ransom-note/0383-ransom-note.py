class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq = {}
        for i in magazine:
            freq[i]=freq.get(i,0)+1
        
        for i in ransomNote:
            if i in freq and freq[i]>0 :
                freq[i] -= 1
            else:
                return False
        else:
            return True
