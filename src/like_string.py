#字符串相似度
a = input()
b = input()
def get_n(s):
    tmp = {}
    s_n = []
    cnt = 0
    for c in s:
        if c not in tmp:
            tmp[c] = cnt
            cnt += 1
        s_n.append(tmp[c])
    return s_n
b_n = get_n(b)
a_n = get_n(a)
cnt = 0
for i in range(len(a) - len(b) + 1):
    sub_b_n = [j+a_n[i] for j in b_n]
    if sum(list(map(lambda x:x[0] - x[1], zip(a_n[i:i+len(b)], sub_b_n)))) == 0:
        cnt += 1
print(cnt) 
