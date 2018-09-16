#三角形元组数
l = [int(i) for i in input().split()]
l.sort()
x, y, z = l[0], l[1], l[2]
cnt = 0
for i in range(z, 0, -1):
    p1, p2 = 1, y
    while p1 <= x and p2 > 0:
        if p1 + p2 < i:
            p1 += 1
        elif p1 + p2 > i:
            p2 -= 1
        else:
            cnt += 1
print(cnt)