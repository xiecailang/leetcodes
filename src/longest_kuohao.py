'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
'''
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max_len = 0
        left = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    top_ = stack.pop()
                    if len(stack) == 0:
                        max_len = max(max_len, i - left + 1)
                    else:
                        max_len = max(max_len, i - stack[len(stack) - 1])
                else:
                    left = i + 1


        return max_len

s = input()
so = Solution()
print(so.longestValidParentheses(s))