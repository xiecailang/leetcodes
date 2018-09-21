'''
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
'''
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(2, len(p) + 1, 2):
            dp[0][j] = dp[0][j-2] and p[j - 1] == '*'
        for i in range(1, len(s) + 1):
            for j in range(1, len(p)+1):       
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j - 2] and (s[i - 1] == p[j - 2] or p[j-2] == '.')) or (dp[i -1][j] and (s[i - 1] == p[j - 2] or p[j-2] == '.'))
        return dp[len(s)][len(p)]
s, p = input(), input()
so = Solution()
print(so.isMatch(s, p))