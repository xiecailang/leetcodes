#贪吃的小Q
n, m =[int(i) for i in input().split()]

def cal_sum(s):
    t_sum = 0
    for i in range(n):
        t_sum += s
        s = (s + 1)//2 #向上取整
    return t_sum

low, high = 1, m
while low <= high:
    mid = (low + high)//2
    if cal_sum(mid) == m:
        print(mid)
        break
    elif cal_sum(mid) < m:
        low = mid + 1
    else:
        high = mid - 1
if low > high:
    print(low - 1)