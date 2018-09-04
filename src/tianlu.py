#天路
[n, m] = [int(i) for i in input().split()]
v = []
for i in range (m):
    v.append([int(j) for j in input().split()])
cnt = [0] * n

for a in v:
    cnt[a[0]-1] += 1
    cnt[a[1]-1] += 1
ans = list(filter(lambda x:x==1, cnt))
print(0 if len(ans) <= 2 else len(ans) - 2)
