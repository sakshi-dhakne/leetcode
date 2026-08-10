class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.st = []

        for i in s:
            if (i=='{' or i=='[' or i=='('):
                self.st.append(i)
            
            else:
                if len(self.st)==0:
                    return False
                
                j = self.st.pop()
                if ((i=='}'and j=='{')or(i==']'and j=='[')or(i==')'and j=='(')):
                    continue
                else:
                    return False

        return len(self.st)==0

