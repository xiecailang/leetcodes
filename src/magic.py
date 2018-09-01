#Magic
a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}
avg_a, sum_a = 0, sum(a)
avg_b, sum_b = 0, sum(b)

avg_a = sum_a/len(a)
avg_b = sum_b/len(b)
i = 0
cnt = 0
for key in list(b):
    avg_a_ = (sum_a + key)/(len(a) + 1)
    avg_b_ = (sum_b - key)/(len(b) - 1)
    if avg_a < avg_a_ and avg_b < avg_b_:      
        sum_a = sum_a + key
        sum_b = sum_b - key
        b.remove(key)
        a.add(key)
        cnt += 1
        print(key,end = ',')
    else:
        i += 1
print(cnt)