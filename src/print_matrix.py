#顺时针打印矩阵
all_data = []
data_size = []
while True:
    [m, n] = [int(i) for i in input().split()]
    if m == -1 and n == -1:
        break
    data_size.append([m, n])
    data_ = []
    a = None
    for i in range(m):
        a = [int(i) for i in input().split()]
        data_.append(a)
    all_data.append(data_)

def print_outside(data, ans, row_start, row_end, col_start, col_end):
    for i in range(col_start, col_end, 1):
        ans.append(data[row_start][i])
    for i in range(row_start, row_end, 1):
        ans.append(data[i][col_end])
    for i in range(col_end, col_start, -1):
        ans.append(data[row_end][i])
    for i in range(row_end, row_start, -1):
        ans.append(data[i][col_start])

def print_matrix(data, ans, row_start, row_end, col_start, col_end):
    if row_end < row_start or col_end < col_start:
        return 
    if row_end == row_start and col_end == col_start:
        ans.append(data[row_start][col_start])
        return 
    print_outside(data, ans, row_start, row_end, col_start, col_end)
    print_matrix(data, ans, row_start + 1, row_end - 1, col_start + 1, col_end - 1)
for i in range(len(all_data)):
    d = all_data[i]
    ans = []
    [m, n] = data_size[i]
    print_matrix(d, ans, 0, m - 1, 0, n - 1)
    print(','.join(str(i) for i in ans))
