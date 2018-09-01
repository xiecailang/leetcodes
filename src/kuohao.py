#括号匹配
str_ = list(input())
stack = []
cnt = 0
over_cnt = 0
for c in str_:
    if c == '(':
        stack.append(c)
    elif c == ')':
        if len(stack) > 0:
            stack.pop(-1)
        else:
            over_cnt += 1
    cnt += 1

print('Yes' if cnt == len(str_) and over_cnt <= 1 else 'No')





