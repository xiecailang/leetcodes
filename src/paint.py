#AI绘画
'''
2
2 2
C B
W C
3 3
W C Y
W b R
W Y W
'''
a = ['a', 'b']
c = list(set(a).difference(set(['a'])))

X = int(input())
data = []
data_size = []
for i in range(X):
    [N, K] = [int(i) for i in input().split()]
    data_size.append([N, K])
    sub_data = []
    for j in range(N):
        sub_data.append(input().split())
    data.append(sub_data)

#预处理
for k in range(X):
    for i in range(len(data[k])):
        for j in range(len(data[k][i])):
            if data[k][i][j] == 'B':
                data[k][i][j] = ['C','M']
            elif data[k][i][j] == 'R':
                data[k][i][j] = ['M', 'Y']
            elif data[k][i][j] == 'G':
                data[k][i][j] = ['Y', 'C']
            elif data[k][i][j] == 'b':
                data[k][i][j] = ['C', 'Y', 'M']

def dp(data_, row, col, n, k):
    if row > n or col > k:
        return 
    if data_[row][col] in ['C', 'M', 'Y']:
        #左边
        if col > 0 and data_[row][col - 1] != 'W' and data_[row][col] in data_[row][col - 1]:
            data_[row][col - 1] = list(set(data_[row][col - 1]).difference(set(data_[row][col])))
            if len(data_[row][col - 1] ) == 0:
                data_[row][col - 1] = 'W'
        #右边
        elif col < k - 1 and data_[row][col + 1] != 'W' and data_[row][col] in data_[row][col + 1]:
            data_[row][col + 1] = list(set(data_[row][col + 1]).difference(set(data_[row][col])))
            if len(data_[row][col + 1] ) == 0:
                data_[row][col + 1] = 'W'
        #上边
        elif row > 0 and data_[row - 1][col] != 'W' and data_[row][col] in data_[row - 1][col]:
            data_[row - 1][col] = list(set(data_[row - 1][col]).difference(set(data_[row][col])))
            if len(data_[row - 1][col]) == 0:
                data_[row - 1][col] = 'W'
        elif row < n - 1 and data_[row + 1][col] != 'W' and data_[row][col] in data_[row + 1][col]:
            data_[row + 1][col] = list(set(data_[row + 1][col]).difference(set(data_[row][col])))
            if len(data_[row + 1][col]) == 0:
                data_[row + 1][col] = 'W'
        data_[row][col] = 'W'

for k in range(X):
    data_ = data[k]
    [n, k] = data_size[k]
    for i in range(n):
        for j in range(k):
            dp(data_, i, j, n, k)
    for i in range(n):
        for j in range(k):
            dp(data_, i, j, n, k)
    flag = True
    for i in range(len(data_)):
        for j in range(len(data_[i])):
            if len(set(data_[i][j]).difference(set(['W']))) > 0:
                flag = False
                break
    print('true' if flag else 'false')
