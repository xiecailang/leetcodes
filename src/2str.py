#双生字符串
def move_str(str_, n):
    return str_[n:len(str_)]+str_[0:n]
def turn_str(str_):
    return str_[::-1]
    
t = int(input())
ans = []
strs_input = []
for i in range(t):
    n = int(input())
    strs = []
    for j in range(n):
        strs.append(input())
    strs_input.append(strs)

for strs in strs_input:
    mod = strs[0]
    cnt  = 0
    for j in range(1, len(strs), 1):
        for k in range(len(strs[j])):
            move_k = move_str(strs[j], k)
            if mod == move_k or mod == turn_str(move_k):
                cnt += 1
                break
    if cnt + 1 == len(strs):
        ans.append('Yeah')
    else:
        ans.append('Sad')
for an in ans:
    print(an)
#print(ans)