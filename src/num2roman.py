class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        from collections import OrderedDict
        dic = OrderedDict([('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)])
        res = ''
        for key in dic:
            h = int(num / dic[key])
            if h == 0:
                continue
            res = '%s%s' % (res, key*h)
            num = num - h*dic[key]
        return res
solution = Solution()
print(solution.intToRoman(4))