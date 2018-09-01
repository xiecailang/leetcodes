#直播
class node:
    def __init__(self, s, t):
        self.s = s
        self.t = t
        self.d = abs(t - s)
            
def is_combine(node1, node2):
    if node1.t < node2.s or node2.t < node1.s:
        return False
    else:
        return True

n = int(input())
m = int(input())
st_ = [int(i) for i in input().split()]
st = []
idx = 0
while idx+1 < len(st_):
    st.append(node(st_[idx], st_[idx +1]))
    idx += 2
st.sort(key=lambda x:x.d)
ans = []
cnt = 0
for i in range(len(st)):
    if(cnt > m):
        break
    if len(ans) == 0:
        ans.append(st[i])
        cnt+= (st[i].d)
    else:
        for j in range(len(ans)):
            if cnt > m:
                break
            if not is_combine(ans[j], st[i]):
                ans.append(st[i])
                cnt += st[i].d

print(len(ans))

