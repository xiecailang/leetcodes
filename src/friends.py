#朋友分组
n = int(input())
rela = []
for i in range(n):
    rela.append([int(j) for j in input().split()])
ans = []

def getsub(index, nums):
    sub = [index]
    for i in range(len(nums)):
        sub.append(nums[i], getsub(i))
    return sub

for i in range(len(rela)):
    sub = [i]
    for j in range(len(rela[i])):
        if rela[i][j] == 0:
            break
        sub = getsub(j, rela[i][j])
    ans.append(sub)
