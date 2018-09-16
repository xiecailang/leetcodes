#游戏
import math
[x, y] = [int(i) for i in input().split()]
n1 = (-1 + math.sqrt(1+8*(x+y)))/2.0
n2 = (-1 - math.sqrt(1+8*(x+y)))/2.0
N = n1 if n1 == int(n1) and n1 > 0 else n2
ans = 0
def f_sum(n, k):
    global ans
    if k - n <= 0:
        ans += 1
        return
    else:
        ans += 1
        return f_sum(n - 1, k - n)
if N<x:
    f_sum(N, x)
else:
    ans = 1
print(ans)
