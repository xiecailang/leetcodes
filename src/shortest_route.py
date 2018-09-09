'''
给定一张包含N个点、N-1条边的无向连通图，节点从1到N编号，每条边的长度均为1。假设你从1号节点出发并打算遍历所有节点，那么总路程至少是多少？
输入
第一行包含一个整数N，1≤N≤105。
接下来N-1行，每行包含两个整数X和Y，表示X号节点和Y号节点之间有一条边，1≤X，Y≤N。

输出
输出总路程的最小值。
'''
import numpy as np
N = int(input())
matrix = np.zeros((N, N))
for i in range(N-1):
    [x, y] = [int(j)-1 for j in input().split()]
    matrix[x][y], matrix[y][x] = 1, 1

t_cnt = []
def fun(i, j):
    if matrix[i][j] == 0 or i >= N or j >= N:
        return 0
    for k in range(N):
        sub_cnt = 0
        for m in range(k+1, N):
            if matrix[k][m] == 1:
                sub_cnt += 1
                sub_cnt += fun(m, k+1)
        t_cnt.append(sub_cnt)
fun(0, 1)
x = np.sum(np.multiply(t_cnt, 2)) - 2*max(t_cnt) + max(t_cnt)
print(x)

