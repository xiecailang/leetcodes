#神奇数

def isMagic(n):
    nums = []
    sum_ = 0
    while n > 0:
        temp = n % 10
        sum_ += temp
        nums.append(temp)
        n -= temp
        n = int(n/10)
    if sum_ % 2 != 0:
        return False
    else: 
        #nums.sort()
        low, high = 0, len(nums) - 1
        flag = False
        sum_sub = int(sum_/2)
        cur_sum = sum_
        while low <= high:
            cur_sum -= nums[low]
            low += 1
            if cur_sum == sum_sub:
                flag = True
                break
            cur_sum -= nums[high]
            high -= 1
            if cur_sum == sum_sub:
                flag = True
                break
        return flag

l_, r = [int(i) for i in input().split()]
cnt = 0
if r <= 10:
    print(0)
else:
    for i in range(l_, r+1, 1):
        if isMagic(i):
            cnt += 1
    print(cnt)