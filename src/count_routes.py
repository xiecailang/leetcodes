#滴滴，查找轨迹数量
N = int(input())
data = []
for i in range(N):
    M = int(input())
    sub_data = []
    for j in range(M):
        tmp = input().split()
        sub_data.append(tmp)
    data.append(sub_data)
def is_interside(a, b, c, d):
    x1, y1 = int(a[0]), int(a[1])
    x2, y2 = int(b[0]), int(b[1])
    x3, y3 = int(c[0]), int(c[1])
    x4, y4 = int(d[0]), int(d[1])
    f1 = (y3 - y1)*(x1 - x2) - (x3 - x1)*(y1 - y2)
    f2 = (y4 - y1)*(x1 - x2) - (x4 - x1)*(y1 - y2)
    if f1 * f2 > 0:
        return False
    return True
def is_cross(s1, s2):
    a = s1[1:3]
    b = s1[3:]
    c = s2[1:3]
    d = s2[3:]
    if not is_interside(a, b, c, d):
        return False
    if not is_interside(c, d, a, b):
        return False
    return True

def cnt_cross(s, data):
    if len(data) == 1:
        return 1
    cnt = 0
    for i in range(len(data)):
        if is_cross(s, data[i]):
            cnt += cnt_cross(data[i], data[0:i]+data[i+1:])
    return cnt

ans = []
for d in data:
    cur_data = []
    for s in d:
        if s[0] == 'T':
            cur_data.append(s)
        else:#'Q'
            index = int(s[1])-1
            dic = {}
            for j in range(len(cur_data)):
                for k in range(len(cur_data)):
                    if is_cross(cur_data[j], cur_data[k]):
                        if j not in dic:
                            dic[j] = []
                        dic[j].append(k)
            len_ = len(dic[index])
            for key in range(len_):
                dic[index].extend(dic[index][key])
            print(len(list(set(dic[index]))))
    print()