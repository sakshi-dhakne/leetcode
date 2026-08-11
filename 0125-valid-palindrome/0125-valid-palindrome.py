class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = ''
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
                
        if clean[::-1]==clean:
            return True
        else:
            return False