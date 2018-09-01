class Solution:
    def isNumber2(self, s):
        try:
            float(s)
            return True
        except:
            return False
    def isNumber(self, s):
        """ 
        :type s: str
        :rtype: bool
        """
        import re
        value = re.compile(r'^\s*[-+]?[0-9]+\.?[0-9]*\s*$|^\s*[-+]?[0-9]*\.?[0-9]+\s*$|^\s*[-+]?[0-9]+\.?[0-9]*e[-+]?[0-9]+\s*$|^\s*[-+]?[0-9]*\.?[0-9]+e[-+]?[0-9]+\s*$')

        res = value.match(s)
        if res:
            return True
        else:
            return False

solution = Solution()
print(solution.isNumber2('sn'))
