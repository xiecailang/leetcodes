#整除
def gcd(a, b):
    return a if b==0 else gcd(b, a%b)

def lcm(a, b):
    return a * b/gcd(a,b)
def nlcm(nums, n):
    if n == 1:
        return nums[0]
    else:
        return lcm(nums[n - 1], nlcm(nums, n - 1))

n = int(input())
nums = [i for i in range(1, n+1, 1)]
print(nlcm(nums, n))