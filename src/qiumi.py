#世界杯开幕式
m, n = [int(i) for i in input().split(',')]
seats = []
for i in range(m):
    seats.append([int(i) for i in input().split(',')])

def find_one(x, y):
    sub_cnt = 0
    if x >= 0 and x < m and y >=0 and y < n and seats[x][y] == 1:
        seats[x][y] = 0
        sub_cnt += 1
        sub_cnt += find_one(x - 1, y + 1)
        sub_cnt += find_one(x, y+1)
        sub_cnt += find_one(x+1, y+1)
        sub_cnt += find_one(x+1, y)
        sub_cnt += find_one(x+1, y-1)
        sub_cnt += find_one(x, y-1)
        sub_cnt += find_one(x-1, y-1)
        sub_cnt += find_one(x-1,y)
    return sub_cnt
cnt = 0
max_ = -1
for i in range(m):
    for j in range(n):
        if seats[i][j] == 1:
            max_ = max(max_,find_one(i, j))
            cnt += 1
print('%d,%d' % (cnt, max_))