#背包问题
[n, w] = [int(i) for i in input().split()]
values = [int(i) for i in input().split()]
weight = [int(i) for i in input().split()]

dp = [([0] * (w+1)) for i in range(n+1)]

for i in range(1,n+1,1):
    for j in range(1,w+1,1):
        if weight[i - 1] <= j:
            remain_w = j - weight[i - 1]
            dp[i][j] = max(values[i - 1] + dp[i - 1][remain_w], dp[i - 1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp)