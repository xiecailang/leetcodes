'''
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
示例:
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
'''
class Solution:
    def maxSingleRow(self, data):
        s = []
        res = 0
        for i in range(len(data)):
            d = data[i]
            if i == 0:
                s.append(d)
            else:
                if d >= s[-1]:
                    s.append(d)
                else:
                    cnt = 1
                    while len(s) > 0:
                        top = s.pop()
                        res = max(res, cnt * top)
                        cnt += 1
                        if len(s) == 0 or d >= s[-1]:
                            s.extend([d] * cnt)
                            break
        max_h = max([s[i] * (len(s) - i) for i in range(len(s))])
        return max(res, max_h)
        

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        height = [[0 for i in range(n)] for j in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0:
                    height[row][col] = int(matrix[row][col])
                else:
                    height[row][col] = (0 if matrix[row][col] == '0' else height[row - 1][col] + 1)
        s = [self.maxSingleRow(d) for d in height]
        return max(s)

matrix = [
    ["0","0","1","0"],
    ["1","1","1","1"],
    ["1","1","1","1"],
    ["1","1","1","0"],
    ["1","1","0","0"],
    ["1","1","1","1"],
    ["1","1","1","0"]]
so = Solution()
print(so.maximalRectangle(matrix))
