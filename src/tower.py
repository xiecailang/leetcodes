#塔
n,k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

s = 0
m = 0
steps = []
max_index = a.index(max(a))
min_index = a.index(min(a)) 
for i in range(k):
    a[max_index] -= 1
    a[min_index] += 1
    steps.append([max_index + 1, min_index + 1])
    max_index = a.index(max(a))
    min_index = a.index(min(a)) 
    
    temp = a[max_index] - a[min_index]

    s = temp
    m += 1
    
    if temp == 1:
        break
    
    
    

print(s, m)
for c in steps:
    print(c[0], c[1])
