#嗜睡
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]

ans = -1
sum_ = 0
for i in range(len(a)):
    if t[i]:
        sum_ += a[i]

for i in range(0, len(a) - k + 1):
    if t[i]:
        continue
    else:
        sub_sum = sum_
        for j in range(i, i+k):
            if not t[j]:
                sub_sum += a[j]
        ans = max(ans, sub_sum)

print(ans)

