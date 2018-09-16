'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. 
For example, given n = 3, a solution set is: 
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution:
    def dfs(self, left, right, temp, ans):
        if left < right:
            return
        if left == 0 and right == 0:
            ans.append(temp)
        else:
            if left > 0:                
                self.dfs(left - 1, right, temp + ')', ans)
            if right > 0:                
                self.dfs(left, right - 1, temp + '(', ans)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        temp = ''
        self.dfs(n, n, temp, ans)
        return ans
        
    
#print(3//2)
sol = Solution()
n = int(input())
print(sol.generateParenthesis(n))