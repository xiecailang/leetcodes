#纸牌游戏

n = int(input())
nums = [int(i) for i in input().split()]
nums.sort(reverse = True)
sum_a = 0
sum_b = 0
for i in range(n):
    if i % 2 == 0:
        sum_a += nums[i]
    else:
        sum_b += nums[i]

print(sum_a - sum_b)

