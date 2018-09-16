'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
示例 1:
输入: dividend = 10, divisor = 3
输出: 3
示例 2:
输入: dividend = 7, divisor = -3
输出: -2
'''
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = -1 if (dividend < 0 and divisor >0) or (dividend > 0 and divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0
        if dividend == divisor:
            return flag * 1
        if divisor == 1:
            return flag * dividend if flag*dividend < 2**31 else 2**31 - 1
        ans = len(range(divisor, dividend, divisor))
        return flag*(ans + 1) if (ans+1) * divisor == dividend else flag*(ans)

dividend = int(input())
divisor = int(input())
so = Solution()
print(so.divide(dividend, divisor))