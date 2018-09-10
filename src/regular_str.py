#归一化字符串
s = input()
from collections import Counter
cnt = Counter(s).items()
sort_ = sorted(cnt,key=lambda x:x[0])
ans = ''
for c in sort_:
    ans = '%s%c%d' % (ans ,c[0], c[1])
print(ans)
