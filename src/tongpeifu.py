'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。
说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
'''
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i- 1][j-1] and (s[i-1] == p[j -1] or p[j - 1] == '?')
                else:
                    dp[i][j] = dp[i- 1][j-1] or dp[i][j-1] or dp[i-1][j]
        return dp[len(s)][len(p)]
s = input()
p = input()
so = Solution()
print(so.isMatch(s, p))