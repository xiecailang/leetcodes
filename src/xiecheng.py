#KL距离
import math
p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
x = list(set(p) | set(q))

sum_ = 0
for i in x:
    p_f = p.count(i)/len(p)
    q_f = q.count(i)/len(q)
    if q_f == 0:
        sum_ += p_f
    else:
        sum_ += p_f * math.log2(p_f/q_f)

print('%.2f' % sum_)


