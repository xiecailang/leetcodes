#五子棋
data = []
for i in range(15):
    data.append(input())
ans = ''
max_b = 0
max_w = 0
for i in range(15):
    max_b = max(max_b, data[i].count('B'))
    max_w = max(max_w, data[i].count('W'))
for j in range(15):
    col = data[:][j]
    max_b = max(max_b, col.count('B'))
    max_w = max(max_w, col.count('W'))
for i in range(29):
    n, m = 0, i
    col = []
    for j in range(i+1):
        if i < 15 and i - j < n and i - j < 15:
            col.append(data[j][i-j])
    max_b = max(max_b, col.count('B'))
    max_w = max(max_w, col.count('W'))
for i in range(29):  # 共输出 cols * 2 - 1 行
    diff = 15 - i - 1  # 每一行的差
    col = []
    for j in range(15):  # 数组中每一个值的下标范围是0到cols
        k = j - diff  # 通过一个下标值计算另一个下标值
        if k >= 0 and k < 15:  # 剩下就是判断这些下标值是否满足当前的情况， 这一步不怎么好理解
            col.append(data[k][j])
    max_b = max(max_b, col.count('B'))
    max_w = max(max_w, col.count('W'))

if max_b == 5 and max_w <5:
    print('black win')
elif max_w == 5 and max_b < 5:
    print('white win')
elif max_b < 5 and max_w < 5:
    if sum([d.count('.') for d in data]) == 0:
        print('draw')
    else:
        print('not finished')
else:
    print('invalid board')


