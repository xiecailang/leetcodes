class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res_str = ""
        one_len = max(1, numRows + numRows - 2)

        for i in range(0, numRows):
            if i == 0 or i == numRows - 1:
                j = i
                while j < len(s):
                    res_str += s[j]
                    j += one_len
            else:
                j = i
                col = 0
                while j < len(s):
                    res_str += s[j]
                    if(col % 2 == 0):
                        j = j + one_len - i * 2
                    else:
                        j = j + 2 * i
                    col += 1
        return res_str
solution = Solution()
print(solution.convert('A', 1))   