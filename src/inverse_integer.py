
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2**31 or x > 2**31 - 1:
            return 0
        sign = -1 if x < 0 else 1
        temp = sign * x
        res = 0
        while temp > 0:
            i = temp % 10
            res = res * 10 + i
            temp = int(temp/10)
        res *= sign

        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res

solution = Solution()
print(solution.reverse(1534236469))
