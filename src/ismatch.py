class Solution:
    def complie_(self, p):
        res = ""
        i = len(p) - 1
        while i >= 0:
            c = p[i]
            if c == '*':
                res = '%c%c%s' % ('N',p[i - 1],res)
                i -= 1
            else:
                res = '%c%c%s' % ('1',c,res)
            i -= 1
        return res

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':
            return s == ''
        if len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:len(p)]) or (len(s) > 0 and (s[0] == p[0] or p[0]== '.') or self.isMatch(s[1:len(s)], p))
        else:
            return len(s) > 0 and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:len(s)], p[1:len(p)])
        

solution = Solution()
print(solution.isMatch('a','ab*a'))