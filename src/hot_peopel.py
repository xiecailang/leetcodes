#抖音红人
'''
3
3
1 2 2 1 2 3
'''
N = int(input())
M = int(input())
input_data = [int(i) for i in input().split()]
data = {}
cnt = {}
for i in range(N):
    data[i+1] = [i+1]
    cnt[i+1] = 1
for i in range(0, M*2, 2):
    data[input_data[i]] = data[input_data[i]]+[input_data[i+1]]

for key in data.keys():
    for i in data[key]:
        data[key] = list(set(data[key]) | set(data[i]))
for key in data.keys():
    for i in data[key]:
        cnt[i] += 1

print(sum([1 for i in cnt if i == N]))