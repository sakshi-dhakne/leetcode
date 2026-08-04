class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen1 = {}
        seen2 = {}
        for ch1,ch2 in zip(s,t):

            if ch1 in seen1:
               if seen1[ch1] != ch2:
                  return False
                  break

            if ch2 in seen2:   
               if seen2[ch2] != ch1:
                  return False
                  break
            
            seen1[ch1] = ch2
            seen2[ch2] = ch1
        
        return True