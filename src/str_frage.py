str_ = input()
t_sum, cur_sum = 0, 1
cnt = 1
for i in range(len(str_) - 1):
    if str_[i] == str_[i+1]:
        cur_sum += 1
    else:
        t_sum += cur_sum
        cur_sum = 1
        cnt += 1
print(len(str_),cnt)
print(len(str_)/cnt)

