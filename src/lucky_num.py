#幸运数字
[a, b] = [int(i) for i in input().split()]
cnt = 0
for i in range(a, b+1):
    s = str(i)
    flag = True
    for j in range(0, int(len(s)/2)):
        if s[j] == s[len(s)-1-j]:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)