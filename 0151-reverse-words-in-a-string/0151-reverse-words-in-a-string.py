class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sp = s.split()
        rev = sp[::-1]
        join = " ".join(rev)
        return join