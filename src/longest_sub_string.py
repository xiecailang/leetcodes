#最长公共子序列
s1, s2 = input(), input()
dp = [[0 for i in range(len(s1) + 1)] for j in range(len(s1) + 1)]
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[len(s1)][len(s2)])
