#utf8校验
n_ = int(input())
nums_ = [int(i) for i in input().split()]
def check(nums):
    cnt = 0
    for n in nums:
        if cnt == 0:
            if n >> 5 == 0b110:
                cnt = 1
            elif n >> 4 == 0b1110:
                cnt = 2
            elif n >> 3 == 0b11110:
                cnt = 3
            elif n >> 7:
                return False
        else:
            if n >> 6 != 0b10:
                return False
            cnt -= 1
    return cnt == 0
print(1 if check(nums_) else 0)