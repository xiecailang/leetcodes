'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
'''
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i - 1 >=0:
                    dp[i][j] += dp[i-1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[m-1][n-1]
[m, n] = [int(i) for i in input().split()]
so = Solution()
print(so.uniquePaths(m, n))