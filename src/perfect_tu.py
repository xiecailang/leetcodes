#完部图
T = int(input())
data = []
for i in range(T):
    [n, m] = [int(j) for j in input().split()]
    sub_data = [[0 for i in range(n)] for row in range(n)]
    
    for j in range(m):
        [x, y] = [int(k)-1 for k in input().split()]
        sub_data[x][y] = 1
        sub_data[y][x] = 1
    data.append(sub_data)

for d in data:
    flag = True
    nodes = [''.join(map(str,d[0]))]
    for i in range(1, n):
        sub_s = ''.join(map(str,d[i]))
        if sub_s in nodes:
            continue
        elif len(nodes) < 2:
            nodes.append(sub_s)
        else:
            flag = False
            break
    if len(nodes) == 2 and sum(map(int, nodes[0])) + sum(map(int, nodes[1])) != n:
        flag = False
    print('Yes' if flag else 'No')
    