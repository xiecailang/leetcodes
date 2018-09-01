
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            sign = -1 if x < 0 else 1
            temp = sign * x
            res = 0
            while temp > 0:
                res = res * 10 + temp % 10
                temp = int(temp/10)
      
            return res == x

solution = Solution()
print(solution.isPalindrome(-121))
import math
value= -121
firstDigit = int((value / math.pow(10, int(math.floor(math.log10(value))))))
print(firstDigit)