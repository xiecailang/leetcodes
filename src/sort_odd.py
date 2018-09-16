N = int(input())
nums = []
dic1 = {}
t_len = 0
for i in range(N):
    n = int(input())
    nums.append(n)
    if n not in dic1:
        dic1[n] = 1
        t_len += 1
left = 0
right = 0
dic2 = {}
sub_len = 0
ans = []
while left <= len(nums) - t_len and right < len(nums):
    if nums[right] not in dic2:
        dic2[nums[right]] = 1
        sub_len += 1
    else:
        dic2[nums[right]] += 1
    if sub_len == t_len:
        #删除起始点重复
        for i in range(left, right+1):
            if dic2[nums[i]] > 1:
                dic2[nums[i]] -= 1
                left += 1
            else:
                break
        ans.append([left+1, right+1])
        dic2[nums[left]] -= 1
        if dic2[nums[left]] == 0:
            dic2.pop(nums[left])
            sub_len -= 1
        left += 1
    right += 1
print(min([a[1] - a[0] + 1 for a in ans]), end = ' ')
print(len(ans))
print(ans)
