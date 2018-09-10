#爬楼梯，2^n
M = int(input())
N = []
for i in range(M):
    N.append(int(input()))
import math
for i in range(M):
    cur_n = N[i]
    dp = [1 for j in range(cur_n+1)]
    for j in range(2,cur_n + 1):
        sum_ = 0
        n = int(math.log2(j))
        k = 0
        while j - 2**k >=0:        
            sum_ += dp[j - 2**k]
            k += 1
        dp[j] = sum_
    print(dp[len(dp)-1])