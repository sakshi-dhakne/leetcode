class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        s = str(x)
        rev = int(s[::-1])
        
        if x == rev:
            return True
        else:
            return False


