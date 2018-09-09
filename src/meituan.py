'''
小明拿到了一个数列a1 , a2 , ... an ，小明想知道存在多少个区间[l,r]同时满足下列两个条件：
1、r-l+1=k;
2、在a l , a l+1,...ar中，存在一个数至少出现了 t 次。
输出满足条件的区间个数

输入
输入第一行三个整数n,k,t(1≤n,k,t≤105。
第二行 n 个整数，a1 , a2 , ... an (1≤ai≤105)。
输出
输出一个数，问题的答案。

'''
from collections import Counter
[n, k, t] = [int(i) for i in input().split()]
an = [int(i) for i in input().split()]
cnt = 0
for l in range(n - k + 1):
    r = l + k
    print(an[l:r])
    max_cnt = max(Counter(an[l:r]).values())
    if  max_cnt >= t:
        cnt += 1
print(cnt)

