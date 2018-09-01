#画家小Q
n, m = 4, 4
str_  = []
str_.append(list('YXXB'))
str_.append(list('XYGX'))
str_.append(list('XBYY'))
str_.append(list('BXXY'))
cnt = 0

def findY(i, j):
    if i >=0 and i < n and j >=0 and j < m and (str_[i][j] == 'Y' or str_[i][j] == 'G'):
        if str_[i][j] == 'G':
            str_[i][j] = 'B'
        else:
            str_[i][j] = 'X'
        findY(i+1, j+1)
    return
def findB(i, j):
    if i >=0 and i < n and j >=0 and j < m and (str_[i][j] == 'B' or str_[i][j] == 'G'):
        if str_[i][j] == 'G':
            str_[i][j] = 'Y'
        else:
            str_[i][j] = 'X'
        findB(i+1, j-1)
    return
for i in range(n):
    for j in range(m):
        if str_[i][j] == 'Y':
            findY(i, j)
            cnt += 1
        elif str_[i][j] == 'B':
            findB(i, j)
            cnt += 1
        elif str_[i][j] == 'G':
            findY(i, j)
            cnt += 1
            str_[i][j] = 'B'
            findB(i, j)
            cnt += 1

print(cnt)
 


cnt = 0
mark = [([0] * n) for i in range(m)]
for i in range(n):
    for j in range(m):
        if mark[i][j] == 2 or (mark[i][j] == 1 and str_[i][j] != 'G'):
            continue
        if str_[i][j] == 'Y':
            p, q = i+1, j+1
            mark[i][j] += 1
            cnt += 1
            while p < n and q < m:
                if not mark[p][q]:
                    if str_[p][q] == 'Y' or 'G':
                        mark[p][q] += 1
                    else:
                        break
                p += 1
                q += 1
        elif str_[i][j] == 'B':
            p, q = i + 1, j - 1
            mark[i][j] += 1
            cnt += 1
            while p >= 0 and q >= 0:
                if not mark[p][q]:
                    if str_[p][q] == 'B' or 'G':
                        mark[p][q] += 1
                    else:
                        break
                p += 1
                q -= 1
        elif str_[i][j] == 'G':
            p, q = i+1, j+1
            if not mark[i][j]:
                cnt += 2
            elif mark[i][j] == 1:
                cnt += 1
            else:
                continue

            mark[i][j] += 1
            
            while p < n and q < m:
                if not mark[p][q]:
                    if str_[p][q] == 'Y' or 'G':
                        mark[p][q] += 1
                    else:
                        break
                p += 1
                q += 1
            
            p, q = i + 1, j-1
            while p >= 0 and q >= 0:
                if not mark[p][q]:
                    if str_[p][q] == 'B' or 'G':
                        mark[p][q] += 1
                    else:
                        break
                p += 1
                q -= 1
        else:
            mark[i][j] = 1

print(cnt)