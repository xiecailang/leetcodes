#排列不同颜色的球
lst = [m, n, k] = [int(i) for i in input().split()]
lst.sort()
import math
cnt =  math.factorial(lst[2])
cnt += math.factorial(lst[1])/math.factorial(lst[2] + 1 - lst[1])
cnt += math.factorial(lst[0])/math.factorial(lst[2] + lst[1] + 1 - lst[0])
print(int(cnt))