#字符串A，B的系数
k, A, B = int(input()), input(), input()
dicA = {}
for i in range(len(A) - k + 1):
    if A[i:i+k] not in dicA:
        dicA[A[i:i+k]] = 1
cnt = 0
for key in dicA:
    cnt += B.count(key)
print(cnt)