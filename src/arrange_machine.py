#安排机器
class node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
            return 'x='+self.x+', y='+self.y
n,m = 3,3
task_ = [node(10, 20), node(90, 56), node(23, 45)]
machine_ = [node(56, 22), node(53, 45), node(98, 12)]
from operator import attrgetter
sorted(task_, key = attrgetter('x','y'), reverse = True)
sorted(machine_, key = attrgetter('x','y'), reverse = True)

cnt = [0]*105
i, j, k, num, ans = 0, 0,0,0,0

for i in range(m):
    while j<n and task_[i].x <= machine_[j].x:
        cnt[machine_[j].y] += 1
        j += 1
    for k in range(task_[i].y, 101,1):
        if cnt[k]:
            num += 1
            cnt[k] -= 1
            ans += (200 * task_[i].x + 3 * task_[i].y)
            break

print(num, ans)

