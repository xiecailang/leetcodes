#在矩阵中查找数字
[m, n] = [int(i) for i in input().split()]
nums = []
for i in range(m):
    nums.append([int(j) for j in input().split()])
target = int(input())
flag = False
row, col = 0, n-1
while row < m and col >= 0:
    if target == nums[row][col]:
        flag = True
        break
    if target < nums[row][col]:
        col -= 1
    else:
        row += 1
print('true' if flag else 'false')