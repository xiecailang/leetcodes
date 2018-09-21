#最短前缀
n = int(input())
data = []
for i in range(n):
    data.append(input())
ans = []
for i in range(n):
    for j in range(1, len(data[i])):
        sub = data[i][:j]
        flag = False
        for k in range(n):
            if i != k and sub == data[k][:j]:
                flag = True
                break
        if not flag:
            print(sub)
            break

