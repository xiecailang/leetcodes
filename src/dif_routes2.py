'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = 0 if m==0 else len(obstacleGrid[0])

        if m == 0 or n == 0:
            return 0

        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if i - 1 >=0 and obstacleGrid[i][j] == 0:
                    dp[i][j] += dp[i-1][j]
                if j - 1 >= 0 and obstacleGrid[i][j] == 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[m-1][n-1]
grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
so = Solution()
print(so.uniquePathsWithObstacles(grid))
