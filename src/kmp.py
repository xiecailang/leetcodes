def get_next(ps):
    ps = list(ps)
    next_ = [0] * len(ps)
    next_[0] = -1
    j = -1
    i = 0
    while i < len(ps) - 1:
        if j == -1 or ps[i] == ps[j] or ps[i] == '?' or ps[j] == '?':
            i += 1
            j += 1
            next_[i] = j
        else:
            j = next_[j]
    return next_
def search(str_, ps):
    next_ = get_next(ps)
    i,j = 0, 0
    cnt = 0
    t_cnt = 0
    while i < len(str_):
        if j == len(ps):
            j = 0
            cnt += 1
            break
        if j == -1 or str_[i] == ps[j] or ps[j] == '?':
            i += 1
            j += 1
            t_cnt+=1
        else:
            j = next_[j]
        
    if j == len(ps):
        cnt += 1
    return cnt, t_cnt
s = input()
p = input()
print(search(s, p))

'''
ps    A B C D A B D '\0'
next  -1 0 0 0 0 1 2 0
i = 0, j = -1, next = [-1]
i = 1, j = 0, next = [-1, 0]
i = 1, j = -1, next = [-1, 0]
i = 2, j = 0, next = [-1, 0, 0]
i = 2, j = -1, next = [-1, 0, 0]
i = 3, j = 0, next = [-1, 0, 0, 0]
i = 3, j = -1, next = [-1, 0, 0, 0]
i = 4, j = 0, next = [-1, 0, 0, 0, 0]
i = 5, j = 1, next = [-1, 0, 0, 0, 0, 1]
i = 6, j = 2, next = [-1, 0, 0, 0, 0, 1, 2]
'''


