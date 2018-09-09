#组织优化
m = int(input())
nums = []
for i in range(m):
    sub = [int(j) for j in input().split()]
    nums.append(sub)
def cnt_partments(nums_, row, col):
    if 0 <= row < m and 0 <= col < m and nums_[row][col] != 0:
        nums_[row][col] = 0
        cnt_partments(nums_, row, col - 1)
        cnt_partments(nums_, row, col + 1)
        cnt_partments(nums_, row - 1, col)
        cnt_partments(nums_, row + 1, col)
    return
cnt = 0
for i in range(m):
    for j in range(m):
        if nums[i][j] == 1:
            cnt_partments(nums, i, j)
            cnt += 1
print(cnt)