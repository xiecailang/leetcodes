#拼硬币
[n1, n2, m] = [int(i) for i in input().split()]
nums1 = [int(i) for i in input().split()]
nums2 = [int(i) for i in input().split()]
nums1.sort()
nums2.sort()
cnt = 0
for i in range(n2):
    sum_ = m - n2
    low, high = 0, len(nums1) - 1
    while low < high:
        if nums1
print(n1, n2, m)