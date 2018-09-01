class Solution:
    def myAtoi2(self, str):
        first_char = False
        sign = 1
        res = 0
        for c in str:
            if c == ' ' and not first_char:
                continue
            elif c == '-' and not first_char:
                sign = -1
                first_char = True
            elif c == '+' and not first_char:
                first_char = True
            elif ord(c) >= ord('0') and ord(c) <= ord('9'):
                first_char = True
                res = res * 10 + ord(c) - ord('0')
            else:
                break
        res *= sign
        if res < -2**31:
            res = -2**31
        if res > 2**31 - 1:
            res = 2**31 - 1
        return res
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        sign = 1
        first_char = False
        if len(str) == 0:
            return 0
        else:
            i = 0
            while i < len(str):
                c = str[i]
                i += 1
                if not first_char:
                    if c == ' ':
                        continue
                    elif c == '-' or c == '+':
                        sign = -1 if c == '-' else 1
                        first_char = True
                        continue
                    else:
                        first_char = True
                        i = 0 if i - 1 < 0 else i - 1
                        continue
                else:
                    if ord(c) < ord('0') or ord(c) > ord('9'):
                        break
                    res = res * 10 + ord(c) - ord('0')
                
        res *= sign
        if res < -2**31:
            res = -2**31
        if res > 2**31 - 1:
            res = 2**31 - 1
        return res

solution = Solution()
print(solution.myAtoi2('0-1'))