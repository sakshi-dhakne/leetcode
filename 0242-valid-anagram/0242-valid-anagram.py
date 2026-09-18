class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st1 = sorted(s)
        st2 = sorted(t)
        if st1==st2:
            return True
        else:
            return False