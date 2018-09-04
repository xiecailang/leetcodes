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
        if dividend < -2**31 or dividend > 2**31 - 1 or divisor < -2**31 or divisor > 2**31 - 1:
            return 2**31 - 1
        cnt = -1
        sum_ = 0
        flag = 1
        if (dividend < 0 and divisor > 0) or (dividend >0 and divisor <0):
            flag = -1
        abs_dividen = abs(dividend)
        abs_divisor = abs(divisor)
        while sum_ <= abs_dividen:
            cnt += 1
            sum_ += abs_divisor
        
        return cnt*flag
dividend = int(input())
divisor = int(input())
so = Solution()
print(so.divide(dividend, divisor))